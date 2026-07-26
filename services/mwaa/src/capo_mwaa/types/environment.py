"""Generated from Smithy shape ``com.amazonaws.mwaa#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.airflow_configuration_options
    import capo_mwaa.types.airflow_version
    import capo_mwaa.types.celery_executor_queue
    import capo_mwaa.types.created_at
    import capo_mwaa.types.endpoint_management
    import capo_mwaa.types.environment_arn
    import capo_mwaa.types.environment_class
    import capo_mwaa.types.environment_name
    import capo_mwaa.types.environment_status
    import capo_mwaa.types.iam_role_arn
    import capo_mwaa.types.kms_key
    import capo_mwaa.types.last_update
    import capo_mwaa.types.logging_configuration
    import capo_mwaa.types.max_webservers
    import capo_mwaa.types.max_workers
    import capo_mwaa.types.min_webservers
    import capo_mwaa.types.min_workers
    import capo_mwaa.types.network_configuration
    import capo_mwaa.types.relative_path
    import capo_mwaa.types.s3_bucket_arn
    import capo_mwaa.types.s3_object_version
    import capo_mwaa.types.schedulers
    import capo_mwaa.types.tag_map
    import capo_mwaa.types.vpc_endpoint_service_name
    import capo_mwaa.types.webserver_access_mode
    import capo_mwaa.types.webserver_url
    import capo_mwaa.types.weekly_maintenance_window_start


class Environment(TypedDict, closed=True):
    name: NotRequired["capo_mwaa.types.environment_name.EnvironmentName"]
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""
    status: NotRequired["capo_mwaa.types.environment_status.EnvironmentStatus"]
    r"""<p>The status of the Amazon MWAA environment.</p> <p>Valid values:</p> <ul> <li> <p> <code>CREATING</code> - The request to create the environment is in progress.</p> </li> <li> <p> <code>CREATING_SNAPSHOT</code> - The request to update environment details, or upgrade the environment version, is in progress and Amazon MWAA is creating a storage volume snapshot of the Amazon RDS database cluster associated with the environment. A database snapshot is a backup created at a specific point in time. Amazon MWAA uses snapshots to recover environment metadata if the process to update or upgrade an environment fails.</p> </li> <li> <p> <code>CREATE_FAILED</code> - The request to create the environment failed and the environment was not created.</p> </li> <li> <p> <code>AVAILABLE</code> - The request was successful and the environment is ready to use.</p> </li> <li> <p> <code>PENDING</code> - The request was successful, but the process to create the environment is paused until you create the required VPC endpoints in your VPC. After you create the VPC endpoints, the process resumes.</p> </li> <li> <p> <code>UPDATING</code> - The request to update the environment is in progress.</p> </li> <li> <p> <code>ROLLING_BACK</code> - The request to update environment details or upgrade the environment version failed and Amazon MWAA is restoring the environment using the latest storage volume snapshot.</p> </li> <li> <p> <code>DELETING</code> - The request to delete the environment is in progress.</p> </li> <li> <p> <code>DELETED</code> - The request to delete the environment is complete, and the environment has been deleted.</p> </li> <li> <p> <code>UNAVAILABLE</code> - The request failed, but the environment did not return to its previous state and is not stable.</p> </li> <li> <p> <code>UPDATE_FAILED</code> - The request to update the environment failed and the environment was restored to its previous state successfully and is ready to use.</p> </li> <li> <p> <code>MAINTENANCE</code> - The environment is undergoing maintenance. Depending on the type of work Amazon MWAA is performing, your environment might be unavailable during this process. Note that as part of the maintenance work, Amazon MWAA performs with a <code>GRACEFUL</code> <a href=\"https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html#mwaa-UpdateEnvironment-request-WorkerReplacementStrategy\"> <code>workerReplacementStrategy</code> </a>.</p> </li> </ul> <p>You can review our troubleshooting guide for a list of common errors and their solutions. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/troubleshooting.html\">Amazon MWAA troubleshooting</a>.</p>"""
    arn: NotRequired["capo_mwaa.types.environment_arn.EnvironmentArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon MWAA environment.</p>"""
    created_at: NotRequired["capo_mwaa.types.created_at.CreatedAt"]
    """<p>The day and time the environment was created.</p>"""
    webserver_url: NotRequired["capo_mwaa.types.webserver_url.WebserverUrl"]
    r"""<p>The Apache Airflow <i>web server</i> host name for the Amazon MWAA environment. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/access-airflow-ui.html\">Accessing the Apache Airflow UI</a>.</p>"""
    execution_role_arn: NotRequired["capo_mwaa.types.iam_role_arn.IamRoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access Amazon Web Services resources in your environment. For example, <code>arn:aws:iam::123456789:role/my-execution-role</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html\">Amazon MWAA Execution role</a>.</p>"""
    service_role_arn: NotRequired["capo_mwaa.types.iam_role_arn.IamRoleArn"]
    r"""<p>The Amazon Resource Name (ARN) for the service-linked role of the environment. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-slr.html\">Amazon MWAA Service-linked role</a>.</p>"""
    kms_key: NotRequired["capo_mwaa.types.kms_key.KmsKey"]
    """<p>The KMS encryption key used to encrypt the data in your environment.</p>"""
    airflow_version: NotRequired["capo_mwaa.types.airflow_version.AirflowVersion"]
    """<p>The Apache Airflow version on your environment.</p> <p>Valid values: <code>2.7.2</code>, <code>2.8.1</code>, <code>2.9.2</code>, <code>2.10.1</code>, <code>2.10.3</code>, <code>2.11.0</code>, and <code>3.0.6</code>.</p>"""
    source_bucket_arn: NotRequired["capo_mwaa.types.s3_bucket_arn.S3BucketArn"]
    r"""<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, <code>arn:aws:s3:::my-airflow-bucket-unique-name</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html\">Create an Amazon S3 bucket for Amazon MWAA</a>.</p>"""
    dag_s3_path: NotRequired["capo_mwaa.types.relative_path.RelativePath"]
    r"""<p>The relative path to the DAGs folder in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/dags</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html\">Adding or updating DAGs</a>.</p>"""
    plugins_s3_path: NotRequired["capo_mwaa.types.relative_path.RelativePath"]
    r"""<p>The relative path to the file in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/plugins.zip</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html\">Installing custom plugins</a>.</p>"""
    plugins_s3_object_version: NotRequired[
        "capo_mwaa.types.s3_object_version.S3ObjectVersion"
    ]
    r"""<p>The version of the <code>plugins.zip</code> file in your Amazon S3 bucket. You must specify the <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html\">version ID</a> that Amazon S3 assigns to the file.</p> <p> Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: </p> <p> <code>3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo</code> </p> <p>For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html\">Installing custom plugins</a>.</p>"""
    requirements_s3_path: NotRequired["capo_mwaa.types.relative_path.RelativePath"]
    r"""<p>The relative path to the <code>requirements.txt</code> file in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/requirements.txt</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html\">Installing Python dependencies</a>.</p>"""
    requirements_s3_object_version: NotRequired[
        "capo_mwaa.types.s3_object_version.S3ObjectVersion"
    ]
    r"""<p>The version of the <code>requirements.txt </code> file on your Amazon S3 bucket. You must specify the <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html\">version ID</a> that Amazon S3 assigns to the file.</p> <p> Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: </p> <p> <code>3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo</code> </p> <p> For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html\">Installing Python dependencies</a>. </p>"""
    startup_script_s3_path: NotRequired["str"]
    r"""<p>The relative path to the startup shell script in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/startup.sh</code>.</p> <p> Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html\">Using a startup script</a>. </p>"""
    startup_script_s3_object_version: NotRequired["str"]
    r"""<p>The version of the startup shell script in your Amazon S3 bucket. You must specify the <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html\">version ID</a> that Amazon S3 assigns to the file.</p> <p> Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: </p> <p> <code>3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo</code> </p> <p> For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html\">Using a startup script</a>. </p>"""
    airflow_configuration_options: NotRequired[
        "capo_mwaa.types.airflow_configuration_options.AirflowConfigurationOptions"
    ]
    r"""<p>A list of key-value pairs containing the Apache Airflow configuration options attached to your environment. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html\">Apache Airflow configuration options</a>.</p>"""
    environment_class: NotRequired["capo_mwaa.types.environment_class.EnvironmentClass"]
    r"""<p>The environment class type. Valid values: <code>mw1.micro</code>, <code>mw1.small</code>, <code>mw1.medium</code>, <code>mw1.large</code>, <code>mw1.xlarge</code>, and <code>mw1.2xlarge</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html\">Amazon MWAA environment class</a>.</p>"""
    max_workers: NotRequired["capo_mwaa.types.max_workers.MaxWorkers"]
    """<p>The maximum number of workers that run in your environment. For example, <code>20</code>.</p>"""
    network_configuration: NotRequired[
        "capo_mwaa.types.network_configuration.NetworkConfiguration"
    ]
    r"""<p>Describes the VPC networking components used to secure and enable network traffic between the Amazon Web Services resources for your environment. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html\">About networking on Amazon MWAA</a>.</p>"""
    logging_configuration: NotRequired[
        "capo_mwaa.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The Apache Airflow logs published to CloudWatch Logs.</p>"""
    last_update: NotRequired["capo_mwaa.types.last_update.LastUpdate"]
    """<p>The status of the last update on the environment.</p>"""
    weekly_maintenance_window_start: NotRequired[
        "capo_mwaa.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: <code>TUE:03:30</code>.</p>"""
    tags: NotRequired["capo_mwaa.types.tag_map.TagMap"]
    r"""<p>The key-value tag pairs associated to your environment. For example, <code>\"Environment\": \"Staging\"</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a>.</p>"""
    webserver_access_mode: NotRequired[
        "capo_mwaa.types.webserver_access_mode.WebserverAccessMode"
    ]
    r"""<p>The Apache Airflow <i>web server</i> access mode. For more information, refer to <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html\">Apache Airflow access modes</a>.</p> <p>If set to <code>PUBLIC_AND_PRIVATE</code>, creates both a public network load balancer (NLB) for browser access and a private VPC endpoint (VPCE) for worker-to-webserver communication. This mode is only available for Apache Airflow version 3.2 and later.</p>"""
    min_workers: NotRequired["capo_mwaa.types.min_workers.MinWorkers"]
    """<p>The minimum number of workers that run in your environment. For example, <code>2</code>.</p>"""
    schedulers: NotRequired["capo_mwaa.types.schedulers.Schedulers"]
    """<p>The number of Apache Airflow schedulers that run in your Amazon MWAA environment.</p>"""
    webserver_vpc_endpoint_service: NotRequired[
        "capo_mwaa.types.vpc_endpoint_service_name.VpcEndpointServiceName"
    ]
    """<p>The VPC endpoint for the environment's web server.</p>"""
    database_vpc_endpoint_service: NotRequired[
        "capo_mwaa.types.vpc_endpoint_service_name.VpcEndpointServiceName"
    ]
    """<p>The VPC endpoint for the environment's Amazon RDS database.</p>"""
    celery_executor_queue: NotRequired[
        "capo_mwaa.types.celery_executor_queue.CeleryExecutorQueue"
    ]
    r"""<p>The queue ARN for the environment's <a href=\"https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html\">Celery Executor</a>. Amazon MWAA uses a Celery Executor to distribute tasks across multiple workers. When you create an environment in a shared VPC, you must provide access to the Celery Executor queue from your VPC.</p>"""
    endpoint_management: NotRequired[
        "capo_mwaa.types.endpoint_management.EndpointManagement"
    ]
    """<p>Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA. If set to <code>SERVICE</code>, Amazon MWAA will create and manage the required VPC endpoints in your VPC. If set to <code>CUSTOMER</code>, you must create, and manage, the VPC endpoints in your VPC.</p>"""
    min_webservers: NotRequired["capo_mwaa.types.min_webservers.MinWebservers"]
    """<p> The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>"""
    max_webservers: NotRequired["capo_mwaa.types.max_webservers.MaxWebservers"]
    """<p> The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in <code>MaxWebserers</code>. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environment) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import capo_mwaa.types.created_at

        out["CreatedAt"] = capo_mwaa.types.created_at.serialize_json(
            value["created_at"]
        )
    if "webserver_url" in value:
        out["WebserverUrl"] = value["webserver_url"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "service_role_arn" in value:
        out["ServiceRoleArn"] = value["service_role_arn"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "airflow_version" in value:
        out["AirflowVersion"] = value["airflow_version"]
    if "source_bucket_arn" in value:
        out["SourceBucketArn"] = value["source_bucket_arn"]
    if "dag_s3_path" in value:
        out["DagS3Path"] = value["dag_s3_path"]
    if "plugins_s3_path" in value:
        out["PluginsS3Path"] = value["plugins_s3_path"]
    if "plugins_s3_object_version" in value:
        out["PluginsS3ObjectVersion"] = value["plugins_s3_object_version"]
    if "requirements_s3_path" in value:
        out["RequirementsS3Path"] = value["requirements_s3_path"]
    if "requirements_s3_object_version" in value:
        out["RequirementsS3ObjectVersion"] = value["requirements_s3_object_version"]
    if "startup_script_s3_path" in value:
        out["StartupScriptS3Path"] = value["startup_script_s3_path"]
    if "startup_script_s3_object_version" in value:
        out["StartupScriptS3ObjectVersion"] = value["startup_script_s3_object_version"]
    if "airflow_configuration_options" in value:
        import capo_mwaa.types.airflow_configuration_options

        out["AirflowConfigurationOptions"] = (
            capo_mwaa.types.airflow_configuration_options.serialize_json(
                value["airflow_configuration_options"]
            )
        )
    if "environment_class" in value:
        out["EnvironmentClass"] = value["environment_class"]
    if "max_workers" in value:
        out["MaxWorkers"] = value["max_workers"]
    if "network_configuration" in value:
        import capo_mwaa.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_mwaa.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "logging_configuration" in value:
        import capo_mwaa.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_mwaa.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "last_update" in value:
        import capo_mwaa.types.last_update

        out["LastUpdate"] = capo_mwaa.types.last_update.serialize_json(
            value["last_update"]
        )
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "tags" in value:
        import capo_mwaa.types.tag_map

        out["Tags"] = capo_mwaa.types.tag_map.serialize_json(value["tags"])
    if "webserver_access_mode" in value:
        out["WebserverAccessMode"] = value["webserver_access_mode"]
    if "min_workers" in value:
        out["MinWorkers"] = value["min_workers"]
    if "schedulers" in value:
        out["Schedulers"] = value["schedulers"]
    if "webserver_vpc_endpoint_service" in value:
        out["WebserverVpcEndpointService"] = value["webserver_vpc_endpoint_service"]
    if "database_vpc_endpoint_service" in value:
        out["DatabaseVpcEndpointService"] = value["database_vpc_endpoint_service"]
    if "celery_executor_queue" in value:
        out["CeleryExecutorQueue"] = value["celery_executor_queue"]
    if "endpoint_management" in value:
        out["EndpointManagement"] = value["endpoint_management"]
    if "min_webservers" in value:
        out["MinWebservers"] = value["min_webservers"]
    if "max_webservers" in value:
        out["MaxWebservers"] = value["max_webservers"]
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedAt" in data:
        import capo_mwaa.types.created_at

        out["created_at"] = capo_mwaa.types.created_at.deserialize_json(
            data["CreatedAt"]
        )
    if "WebserverUrl" in data:
        out["webserver_url"] = data["WebserverUrl"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "ServiceRoleArn" in data:
        out["service_role_arn"] = data["ServiceRoleArn"]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    if "AirflowVersion" in data:
        out["airflow_version"] = data["AirflowVersion"]
    if "SourceBucketArn" in data:
        out["source_bucket_arn"] = data["SourceBucketArn"]
    if "DagS3Path" in data:
        out["dag_s3_path"] = data["DagS3Path"]
    if "PluginsS3Path" in data:
        out["plugins_s3_path"] = data["PluginsS3Path"]
    if "PluginsS3ObjectVersion" in data:
        out["plugins_s3_object_version"] = data["PluginsS3ObjectVersion"]
    if "RequirementsS3Path" in data:
        out["requirements_s3_path"] = data["RequirementsS3Path"]
    if "RequirementsS3ObjectVersion" in data:
        out["requirements_s3_object_version"] = data["RequirementsS3ObjectVersion"]
    if "StartupScriptS3Path" in data:
        out["startup_script_s3_path"] = data["StartupScriptS3Path"]
    if "StartupScriptS3ObjectVersion" in data:
        out["startup_script_s3_object_version"] = data["StartupScriptS3ObjectVersion"]
    if "AirflowConfigurationOptions" in data:
        import capo_mwaa.types.airflow_configuration_options

        out["airflow_configuration_options"] = (
            capo_mwaa.types.airflow_configuration_options.deserialize_json(
                data["AirflowConfigurationOptions"]
            )
        )
    if "EnvironmentClass" in data:
        out["environment_class"] = data["EnvironmentClass"]
    if "MaxWorkers" in data:
        out["max_workers"] = data["MaxWorkers"]
    if "NetworkConfiguration" in data:
        import capo_mwaa.types.network_configuration

        out["network_configuration"] = (
            capo_mwaa.types.network_configuration.deserialize_json(
                data["NetworkConfiguration"]
            )
        )
    if "LoggingConfiguration" in data:
        import capo_mwaa.types.logging_configuration

        out["logging_configuration"] = (
            capo_mwaa.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    if "LastUpdate" in data:
        import capo_mwaa.types.last_update

        out["last_update"] = capo_mwaa.types.last_update.deserialize_json(
            data["LastUpdate"]
        )
    if "WeeklyMaintenanceWindowStart" in data:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if "Tags" in data:
        import capo_mwaa.types.tag_map

        out["tags"] = capo_mwaa.types.tag_map.deserialize_json(data["Tags"])
    if "WebserverAccessMode" in data:
        out["webserver_access_mode"] = data["WebserverAccessMode"]
    if "MinWorkers" in data:
        out["min_workers"] = data["MinWorkers"]
    if "Schedulers" in data:
        out["schedulers"] = data["Schedulers"]
    if "WebserverVpcEndpointService" in data:
        out["webserver_vpc_endpoint_service"] = data["WebserverVpcEndpointService"]
    if "DatabaseVpcEndpointService" in data:
        out["database_vpc_endpoint_service"] = data["DatabaseVpcEndpointService"]
    if "CeleryExecutorQueue" in data:
        out["celery_executor_queue"] = data["CeleryExecutorQueue"]
    if "EndpointManagement" in data:
        out["endpoint_management"] = data["EndpointManagement"]
    if "MinWebservers" in data:
        out["min_webservers"] = data["MinWebservers"]
    if "MaxWebservers" in data:
        out["max_webservers"] = data["MaxWebservers"]
    return out
