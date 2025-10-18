use datalake_local;
create table log_processamento (
	id INT,
	data_execucao DATETIME NOT NULL DEFAULT GETDATE(),
	mensagem VARCHAR(255) NOT NULL,
	primary key(id)
);
