"""Generated from Smithy shape ``com.amazonaws.mq#mq``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_mq._auth._signers
import aws_sdk_mq._auth._sigv4
from aws_sdk_mq._auth._identity import Credentials
from aws_sdk_mq._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mq._auth._zapros_handler import AuthMiddleware
from aws_sdk_mq._pagination import resolve_path as _resolve_path
from aws_sdk_mq._services._aws_config import aws_config
from aws_sdk_mq._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__list_of_user
    import aws_sdk_mq.types.__map_of__string
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.authentication_strategy
    import aws_sdk_mq.types.broker_storage_type
    import aws_sdk_mq.types.broker_summary
    import aws_sdk_mq.types.configuration_id
    import aws_sdk_mq.types.create_broker_request
    import aws_sdk_mq.types.create_broker_response
    import aws_sdk_mq.types.create_configuration_request
    import aws_sdk_mq.types.create_configuration_response
    import aws_sdk_mq.types.create_tags_request
    import aws_sdk_mq.types.create_user_request
    import aws_sdk_mq.types.create_user_response
    import aws_sdk_mq.types.data_replication_mode
    import aws_sdk_mq.types.delete_broker_request
    import aws_sdk_mq.types.delete_broker_response
    import aws_sdk_mq.types.delete_configuration_request
    import aws_sdk_mq.types.delete_configuration_response
    import aws_sdk_mq.types.delete_tags_request
    import aws_sdk_mq.types.delete_user_request
    import aws_sdk_mq.types.delete_user_response
    import aws_sdk_mq.types.deployment_mode
    import aws_sdk_mq.types.describe_broker_engine_types_request
    import aws_sdk_mq.types.describe_broker_engine_types_response
    import aws_sdk_mq.types.describe_broker_instance_options_request
    import aws_sdk_mq.types.describe_broker_instance_options_response
    import aws_sdk_mq.types.describe_broker_request
    import aws_sdk_mq.types.describe_broker_response
    import aws_sdk_mq.types.describe_configuration_request
    import aws_sdk_mq.types.describe_configuration_response
    import aws_sdk_mq.types.describe_configuration_revision_request
    import aws_sdk_mq.types.describe_configuration_revision_response
    import aws_sdk_mq.types.describe_user_request
    import aws_sdk_mq.types.describe_user_response
    import aws_sdk_mq.types.encryption_options
    import aws_sdk_mq.types.engine_type
    import aws_sdk_mq.types.ldap_server_metadata_input
    import aws_sdk_mq.types.list_brokers_request
    import aws_sdk_mq.types.list_brokers_response
    import aws_sdk_mq.types.list_configuration_revisions_request
    import aws_sdk_mq.types.list_configuration_revisions_response
    import aws_sdk_mq.types.list_configurations_request
    import aws_sdk_mq.types.list_configurations_response
    import aws_sdk_mq.types.list_tags_request
    import aws_sdk_mq.types.list_tags_response
    import aws_sdk_mq.types.list_users_request
    import aws_sdk_mq.types.list_users_response
    import aws_sdk_mq.types.logs
    import aws_sdk_mq.types.max_results
    import aws_sdk_mq.types.promote_mode
    import aws_sdk_mq.types.promote_request
    import aws_sdk_mq.types.promote_response
    import aws_sdk_mq.types.reboot_broker_request
    import aws_sdk_mq.types.reboot_broker_response
    import aws_sdk_mq.types.update_broker_request
    import aws_sdk_mq.types.update_broker_response
    import aws_sdk_mq.types.update_configuration_request
    import aws_sdk_mq.types.update_configuration_response
    import aws_sdk_mq.types.update_user_request
    import aws_sdk_mq.types.update_user_response
    import aws_sdk_mq.types.weekly_start_time


class mqClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class mqClient:
    """A client for the ``mq`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = mqClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[mqClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: mqClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_broker(
        self,
        broker_name: "aws_sdk_mq.types.__string.__string",
        deployment_mode: "aws_sdk_mq.types.deployment_mode.DeploymentMode",
        engine_type: "aws_sdk_mq.types.engine_type.EngineType",
        host_instance_type: "aws_sdk_mq.types.__string.__string",
        publicly_accessible: "aws_sdk_mq.types.__boolean.__boolean",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        authentication_strategy: Optional[
            "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
        ] = None,
        auto_minor_version_upgrade: Optional[
            "aws_sdk_mq.types.__boolean.__boolean"
        ] = None,
        configuration: Optional[
            "aws_sdk_mq.types.configuration_id.ConfigurationId"
        ] = None,
        creator_request_id: Optional["aws_sdk_mq.types.__string.__string"] = None,
        encryption_options: Optional[
            "aws_sdk_mq.types.encryption_options.EncryptionOptions"
        ] = None,
        engine_version: Optional["aws_sdk_mq.types.__string.__string"] = None,
        ldap_server_metadata: Optional[
            "aws_sdk_mq.types.ldap_server_metadata_input.LdapServerMetadataInput"
        ] = None,
        logs: Optional["aws_sdk_mq.types.logs.Logs"] = None,
        maintenance_window_start_time: Optional[
            "aws_sdk_mq.types.weekly_start_time.WeeklyStartTime"
        ] = None,
        security_groups: Optional[
            "aws_sdk_mq.types.__list_of__string.__listOf__string"
        ] = None,
        storage_type: Optional[
            "aws_sdk_mq.types.broker_storage_type.BrokerStorageType"
        ] = None,
        subnet_ids: Optional[
            "aws_sdk_mq.types.__list_of__string.__listOf__string"
        ] = None,
        tags: Optional["aws_sdk_mq.types.__map_of__string.__mapOf__string"] = None,
        users: Optional["aws_sdk_mq.types.__list_of_user.__listOfUser"] = None,
        data_replication_mode: Optional[
            "aws_sdk_mq.types.data_replication_mode.DataReplicationMode"
        ] = None,
        data_replication_primary_broker_arn: Optional[
            "aws_sdk_mq.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_mq.types.create_broker_response.CreateBrokerResponse":
        r"""<p>Creates a broker. Note: This API is asynchronous.</p> <p>To create a broker, you must either use the AmazonMQFullAccess IAM policy or include the following EC2 permissions in your IAM policy.</p> <ul><li><p>ec2:CreateNetworkInterface</p> <p>This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.</p></li> <li><p>ec2:CreateNetworkInterfacePermission</p> <p>This permission is required to attach the ENI to the broker instance.</p></li> <li><p>ec2:DeleteNetworkInterface</p></li> <li><p>ec2:DeleteNetworkInterfacePermission</p></li> <li><p>ec2:DetachNetworkInterface</p></li> <li><p>ec2:DescribeInternetGateways</p></li> <li><p>ec2:DescribeNetworkInterfaces</p></li> <li><p>ec2:DescribeNetworkInterfacePermissions</p></li> <li><p>ec2:DescribeRouteTables</p></li> <li><p>ec2:DescribeSecurityGroups</p></li> <li><p>ec2:DescribeSubnets</p></li> <li><p>ec2:DescribeVpcs</p></li></ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user\">Create an IAM User and Get Your Amazon Web Services Credentials</a> and <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface\">Never Modify or Delete the Amazon MQ Elastic Network Interface</a> in the <i>Amazon MQ Developer Guide</i>.</p>

        Args:
            authentication_strategy: <p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>
            auto_minor_version_upgrade: <p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. Set to true by default, if no value is specified.</p> <note><p>Must be set to true for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.</p></note>
            broker_name: <p>Required. The broker's name. This value must be unique in your Amazon Web Services account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.</p> <important><p>Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.</p></important>
            configuration: <p>A list of information about the configuration.</p>
            creator_request_id: <p>The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action.</p> <note><p>We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesn't require idempotency.</p></note>
            deployment_mode: <p>Required. The broker's deployment mode.</p>
            encryption_options: <p>Encryption options for the broker.</p>
            engine_type: <p>Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>
            engine_version: <p>The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>
            host_instance_type: <p>Required. The broker's instance type.</p>
            ldap_server_metadata: <p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p>
            logs: <p>Enables Amazon CloudWatch logging for brokers.</p>
            maintenance_window_start_time: <p>The parameters that determine the WeeklyStartTime.</p>
            publicly_accessible: <p>Enables connections from applications outside of the VPC that hosts the broker's subnets. Set to false by default, if no value is provided.</p>
            security_groups: <p>The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.</p>
            storage_type: <p>The broker's storage type.</p>
            subnet_ids: <p>The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER_MULTI_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.</p> <important><p>If you specify subnets in a <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html\">shared VPC</a> for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your Amazon Web Services account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your Amazon Web Services account.</p></important>
            tags: <p>Create tags when creating the broker.</p>
            users: <p>The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, an administrative user is required if using simple authentication and authorization. For brokers using OAuth2, this user is optional. When provided, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.</p>
            data_replication_mode: <p>Defines whether this broker is a part of a data replication pair.</p>
            data_replication_primary_broker_arn: <p>The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.create_broker_request.CreateBrokerRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.create_broker_response.CreateBrokerResponse"
        ]:
            import aws_sdk_mq._operations.mq.create_broker

            output, http_response = (
                aws_sdk_mq._operations.mq.create_broker.create_broker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.create_broker_request.CreateBrokerRequest = {}  # type: ignore[typeddict-item]
        if authentication_strategy is not None:
            input_["authentication_strategy"] = authentication_strategy
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        input_["broker_name"] = broker_name
        if configuration is not None:
            input_["configuration"] = configuration
        if creator_request_id is not None:
            input_["creator_request_id"] = creator_request_id
        input_["deployment_mode"] = deployment_mode
        if encryption_options is not None:
            input_["encryption_options"] = encryption_options
        input_["engine_type"] = engine_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        input_["host_instance_type"] = host_instance_type
        if ldap_server_metadata is not None:
            input_["ldap_server_metadata"] = ldap_server_metadata
        if logs is not None:
            input_["logs"] = logs
        if maintenance_window_start_time is not None:
            input_["maintenance_window_start_time"] = maintenance_window_start_time
        input_["publicly_accessible"] = publicly_accessible
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if tags is not None:
            input_["tags"] = tags
        if users is not None:
            input_["users"] = users
        if data_replication_mode is not None:
            input_["data_replication_mode"] = data_replication_mode
        if data_replication_primary_broker_arn is not None:
            input_["data_replication_primary_broker_arn"] = (
                data_replication_primary_broker_arn
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_configuration(
        self,
        engine_type: "aws_sdk_mq.types.engine_type.EngineType",
        name: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        authentication_strategy: Optional[
            "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
        ] = None,
        engine_version: Optional["aws_sdk_mq.types.__string.__string"] = None,
        tags: Optional["aws_sdk_mq.types.__map_of__string.__mapOf__string"] = None,
    ) -> "aws_sdk_mq.types.create_configuration_response.CreateConfigurationResponse":
        r"""<p>Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).</p>

        Args:
            authentication_strategy: <p>Optional. The authentication strategy associated with the configuration. The default is SIMPLE.</p>
            engine_type: <p>Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>
            engine_version: <p>The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>
            name: <p>Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.</p>
            tags: <p>Create tags when creating the configuration.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import aws_sdk_mq._operations.mq.create_configuration

            output, http_response = (
                aws_sdk_mq._operations.mq.create_configuration.create_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.create_configuration_request.CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
        if authentication_strategy is not None:
            input_["authentication_strategy"] = authentication_strategy
        input_["engine_type"] = engine_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_tags(
        self,
        resource_arn: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        tags: Optional["aws_sdk_mq.types.__map_of__string.__mapOf__string"] = None,
    ) -> None:
        """<p>Add a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource tag.</p>
            tags: <p>The key-value pair for the resource tag.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.create_tags_request.CreateTagsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mq._operations.mq.create_tags

            output, http_response = aws_sdk_mq._operations.mq.create_tags.create_tags(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.create_tags_request.CreateTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_user(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        password: "aws_sdk_mq.types.__string.__string",
        username: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        console_access: Optional["aws_sdk_mq.types.__boolean.__boolean"] = None,
        groups: Optional["aws_sdk_mq.types.__list_of__string.__listOf__string"] = None,
        replication_user: Optional["aws_sdk_mq.types.__boolean.__boolean"] = None,
    ) -> "aws_sdk_mq.types.create_user_response.CreateUserResponse":
        """<p>Creates an ActiveMQ user.</p> <important><p>Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.</p></important>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            console_access: <p>Enables access to the ActiveMQ Web Console for the ActiveMQ user.</p>
            groups: <p>The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>
            password: <p>Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=).</p>
            username: <p>The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>
            replication_user: <p>Defines if this user is intended for CRDR replication purposes.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_mq._operations.mq.create_user

            output, http_response = aws_sdk_mq._operations.mq.create_user.create_user(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id
        if console_access is not None:
            input_["console_access"] = console_access
        if groups is not None:
            input_["groups"] = groups
        input_["password"] = password
        input_["username"] = username
        if replication_user is not None:
            input_["replication_user"] = replication_user

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_broker(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.delete_broker_response.DeleteBrokerResponse":
        """<p>Deletes a broker. Note: This API is asynchronous.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.delete_broker_request.DeleteBrokerRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.delete_broker_response.DeleteBrokerResponse"
        ]:
            import aws_sdk_mq._operations.mq.delete_broker

            output, http_response = (
                aws_sdk_mq._operations.mq.delete_broker.delete_broker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.delete_broker_request.DeleteBrokerRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_configuration(
        self,
        configuration_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.delete_configuration_response.DeleteConfigurationResponse":
        """<p>Deletes the specified configuration.</p>

        Args:
            configuration_id: <p>The unique ID that Amazon MQ generates for the configuration.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.delete_configuration_response.DeleteConfigurationResponse"
        ]:
            import aws_sdk_mq._operations.mq.delete_configuration

            output, http_response = (
                aws_sdk_mq._operations.mq.delete_configuration.delete_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.delete_configuration_request.DeleteConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_id"] = configuration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_tags(
        self,
        resource_arn: "aws_sdk_mq.types.__string.__string",
        tag_keys: "aws_sdk_mq.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource tag.</p>
            tag_keys: <p>An array of tag keys to delete</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.delete_tags_request.DeleteTagsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mq._operations.mq.delete_tags

            output, http_response = aws_sdk_mq._operations.mq.delete_tags.delete_tags(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.delete_tags_request.DeleteTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_user(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        username: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes an ActiveMQ user.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            username: <p>The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.delete_user_response.DeleteUserResponse"
        ]:
            import aws_sdk_mq._operations.mq.delete_user

            output, http_response = aws_sdk_mq._operations.mq.delete_user.delete_user(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id
        input_["username"] = username

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_broker(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.describe_broker_response.DescribeBrokerResponse":
        """<p>Returns information about the specified broker.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.describe_broker_request.DescribeBrokerRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.describe_broker_response.DescribeBrokerResponse"
        ]:
            import aws_sdk_mq._operations.mq.describe_broker

            output, http_response = (
                aws_sdk_mq._operations.mq.describe_broker.describe_broker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.describe_broker_request.DescribeBrokerRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_broker_engine_types(
        self,
        *,
        config_overrides: Optional[mqClientConfig] = None,
        engine_type: Optional["aws_sdk_mq.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.describe_broker_engine_types_response.DescribeBrokerEngineTypesResponse":
        """<p>Describe available engine types and versions.</p>

        Args:
            engine_type: <p>Filter response by engine type.</p>
            max_results: <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>
            next_token: <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.describe_broker_engine_types_request.DescribeBrokerEngineTypesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.describe_broker_engine_types_response.DescribeBrokerEngineTypesResponse"
        ]:
            import aws_sdk_mq._operations.mq.describe_broker_engine_types

            output, http_response = (
                aws_sdk_mq._operations.mq.describe_broker_engine_types.describe_broker_engine_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.describe_broker_engine_types_request.DescribeBrokerEngineTypesRequest = {}  # type: ignore[typeddict-item]
        if engine_type is not None:
            input_["engine_type"] = engine_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_broker_instance_options(
        self,
        *,
        config_overrides: Optional[mqClientConfig] = None,
        engine_type: Optional["aws_sdk_mq.types.__string.__string"] = None,
        host_instance_type: Optional["aws_sdk_mq.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
        storage_type: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.describe_broker_instance_options_response.DescribeBrokerInstanceOptionsResponse":
        """<p>Describe available broker instance options.</p>

        Args:
            engine_type: <p>Filter response by engine type.</p>
            host_instance_type: <p>Filter response by host instance type.</p>
            max_results: <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>
            next_token: <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>
            storage_type: <p>Filter response by storage type.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.describe_broker_instance_options_request.DescribeBrokerInstanceOptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.describe_broker_instance_options_response.DescribeBrokerInstanceOptionsResponse"
        ]:
            import aws_sdk_mq._operations.mq.describe_broker_instance_options

            output, http_response = (
                aws_sdk_mq._operations.mq.describe_broker_instance_options.describe_broker_instance_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.describe_broker_instance_options_request.DescribeBrokerInstanceOptionsRequest = {}  # type: ignore[typeddict-item]
        if engine_type is not None:
            input_["engine_type"] = engine_type
        if host_instance_type is not None:
            input_["host_instance_type"] = host_instance_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if storage_type is not None:
            input_["storage_type"] = storage_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_configuration(
        self,
        configuration_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> (
        "aws_sdk_mq.types.describe_configuration_response.DescribeConfigurationResponse"
    ):
        """<p>Returns information about the specified configuration.</p>

        Args:
            configuration_id: <p>The unique ID that Amazon MQ generates for the configuration.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.describe_configuration_request.DescribeConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.describe_configuration_response.DescribeConfigurationResponse"
        ]:
            import aws_sdk_mq._operations.mq.describe_configuration

            output, http_response = (
                aws_sdk_mq._operations.mq.describe_configuration.describe_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.describe_configuration_request.DescribeConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_id"] = configuration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_configuration_revision(
        self,
        configuration_id: "aws_sdk_mq.types.__string.__string",
        configuration_revision: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.describe_configuration_revision_response.DescribeConfigurationRevisionResponse":
        """<p>Returns the specified configuration revision for the specified configuration.</p>

        Args:
            configuration_id: <p>The unique ID that Amazon MQ generates for the configuration.</p>
            configuration_revision: <p>The revision of the configuration.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.describe_configuration_revision_request.DescribeConfigurationRevisionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.describe_configuration_revision_response.DescribeConfigurationRevisionResponse"
        ]:
            import aws_sdk_mq._operations.mq.describe_configuration_revision

            output, http_response = (
                aws_sdk_mq._operations.mq.describe_configuration_revision.describe_configuration_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.describe_configuration_revision_request.DescribeConfigurationRevisionRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_id"] = configuration_id
        input_["configuration_revision"] = configuration_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_user(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        username: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.describe_user_response.DescribeUserResponse":
        """<p>Returns information about an ActiveMQ user.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            username: <p>The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.describe_user_request.DescribeUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.describe_user_response.DescribeUserResponse"
        ]:
            import aws_sdk_mq._operations.mq.describe_user

            output, http_response = (
                aws_sdk_mq._operations.mq.describe_user.describe_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.describe_user_request.DescribeUserRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id
        input_["username"] = username

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_brokers(
        self,
        *,
        config_overrides: Optional[mqClientConfig] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.list_brokers_response.ListBrokersResponse":
        """<p>Returns a list of all brokers.</p>

        Args:
            max_results: <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>
            next_token: <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.list_brokers_request.ListBrokersRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.list_brokers_response.ListBrokersResponse"
        ]:
            import aws_sdk_mq._operations.mq.list_brokers

            output, http_response = aws_sdk_mq._operations.mq.list_brokers.list_brokers(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.list_brokers_request.ListBrokersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_brokers(
        self,
        *,
        config_overrides: Optional[mqClientConfig] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_mq.types.broker_summary.BrokerSummary]":
        _token = next_token
        while True:
            _response = self.list_brokers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("broker_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_configuration_revisions(
        self,
        configuration_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.list_configuration_revisions_response.ListConfigurationRevisionsResponse":
        """<p>Returns a list of all revisions for the specified configuration.</p>

        Args:
            configuration_id: <p>The unique ID that Amazon MQ generates for the configuration.</p>
            max_results: <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>
            next_token: <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.list_configuration_revisions_request.ListConfigurationRevisionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.list_configuration_revisions_response.ListConfigurationRevisionsResponse"
        ]:
            import aws_sdk_mq._operations.mq.list_configuration_revisions

            output, http_response = (
                aws_sdk_mq._operations.mq.list_configuration_revisions.list_configuration_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.list_configuration_revisions_request.ListConfigurationRevisionsRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_id"] = configuration_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_configurations(
        self,
        *,
        config_overrides: Optional[mqClientConfig] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.list_configurations_response.ListConfigurationsResponse":
        """<p>Returns a list of all configurations.</p>

        Args:
            max_results: <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>
            next_token: <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import aws_sdk_mq._operations.mq.list_configurations

            output, http_response = (
                aws_sdk_mq._operations.mq.list_configurations.list_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.list_configurations_request.ListConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags(
        self,
        resource_arn: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.list_tags_response.ListTagsResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource tag.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse["aws_sdk_mq.types.list_tags_response.ListTagsResponse"]:
            import aws_sdk_mq._operations.mq.list_tags

            output, http_response = aws_sdk_mq._operations.mq.list_tags.list_tags(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_users(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        max_results: Optional["aws_sdk_mq.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.list_users_response.ListUsersResponse":
        """<p>Returns a list of all ActiveMQ users.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            max_results: <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>
            next_token: <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.list_users_response.ListUsersResponse"
        ]:
            import aws_sdk_mq._operations.mq.list_users

            output, http_response = aws_sdk_mq._operations.mq.list_users.list_users(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.list_users_request.ListUsersRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def promote(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        mode: "aws_sdk_mq.types.promote_mode.PromoteMode",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.promote_response.PromoteResponse":
        """<p>Promotes a data replication replica broker to the primary broker role.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            mode: <p>The Promote mode requested. Note: Valid values for the parameter are SWITCHOVER, FAILOVER.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.promote_request.PromoteRequest]",
        ) -> OperationResponse["aws_sdk_mq.types.promote_response.PromoteResponse"]:
            import aws_sdk_mq._operations.mq.promote

            output, http_response = aws_sdk_mq._operations.mq.promote.promote(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.promote_request.PromoteRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id
        input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reboot_broker(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
    ) -> "aws_sdk_mq.types.reboot_broker_response.RebootBrokerResponse":
        """<p>Reboots a broker. Note: This API is asynchronous.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.reboot_broker_request.RebootBrokerRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.reboot_broker_response.RebootBrokerResponse"
        ]:
            import aws_sdk_mq._operations.mq.reboot_broker

            output, http_response = (
                aws_sdk_mq._operations.mq.reboot_broker.reboot_broker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.reboot_broker_request.RebootBrokerRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_broker(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        authentication_strategy: Optional[
            "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
        ] = None,
        auto_minor_version_upgrade: Optional[
            "aws_sdk_mq.types.__boolean.__boolean"
        ] = None,
        configuration: Optional[
            "aws_sdk_mq.types.configuration_id.ConfigurationId"
        ] = None,
        engine_version: Optional["aws_sdk_mq.types.__string.__string"] = None,
        host_instance_type: Optional["aws_sdk_mq.types.__string.__string"] = None,
        ldap_server_metadata: Optional[
            "aws_sdk_mq.types.ldap_server_metadata_input.LdapServerMetadataInput"
        ] = None,
        logs: Optional["aws_sdk_mq.types.logs.Logs"] = None,
        maintenance_window_start_time: Optional[
            "aws_sdk_mq.types.weekly_start_time.WeeklyStartTime"
        ] = None,
        security_groups: Optional[
            "aws_sdk_mq.types.__list_of__string.__listOf__string"
        ] = None,
        data_replication_mode: Optional[
            "aws_sdk_mq.types.data_replication_mode.DataReplicationMode"
        ] = None,
    ) -> "aws_sdk_mq.types.update_broker_response.UpdateBrokerResponse":
        r"""<p>Adds a pending configuration change to a broker.</p>

        Args:
            authentication_strategy: <p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>
            auto_minor_version_upgrade: <p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.</p> <note><p>Must be set to true for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.</p></note>
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            configuration: <p>A list of information about the configuration.</p>
            engine_version: <p>The broker engine version. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p> <note><p>When upgrading to ActiveMQ version 5.18 and above or RabbitMQ version 3.13 and above, you must have autoMinorVersionUpgrade set to true for the broker.</p></note>
            host_instance_type: <p>The broker's host instance type to upgrade to. For a list of supported instance types, see <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types\">Broker instance types</a>.</p>
            ldap_server_metadata: <p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p>
            logs: <p>Enables Amazon CloudWatch logging for brokers.</p>
            maintenance_window_start_time: <p>The parameters that determine the WeeklyStartTime.</p>
            security_groups: <p>The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers.</p>
            data_replication_mode: <p>Defines whether this broker is a part of a data replication pair.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.update_broker_request.UpdateBrokerRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.update_broker_response.UpdateBrokerResponse"
        ]:
            import aws_sdk_mq._operations.mq.update_broker

            output, http_response = (
                aws_sdk_mq._operations.mq.update_broker.update_broker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.update_broker_request.UpdateBrokerRequest = {}  # type: ignore[typeddict-item]
        if authentication_strategy is not None:
            input_["authentication_strategy"] = authentication_strategy
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        input_["broker_id"] = broker_id
        if configuration is not None:
            input_["configuration"] = configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if host_instance_type is not None:
            input_["host_instance_type"] = host_instance_type
        if ldap_server_metadata is not None:
            input_["ldap_server_metadata"] = ldap_server_metadata
        if logs is not None:
            input_["logs"] = logs
        if maintenance_window_start_time is not None:
            input_["maintenance_window_start_time"] = maintenance_window_start_time
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if data_replication_mode is not None:
            input_["data_replication_mode"] = data_replication_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_configuration(
        self,
        configuration_id: "aws_sdk_mq.types.__string.__string",
        data: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        description: Optional["aws_sdk_mq.types.__string.__string"] = None,
    ) -> "aws_sdk_mq.types.update_configuration_response.UpdateConfigurationResponse":
        """<p>Updates the specified configuration.</p>

        Args:
            configuration_id: <p>The unique ID that Amazon MQ generates for the configuration.</p>
            data: <p>Amazon MQ for Active MQ: The base64-encoded XML configuration. Amazon MQ for RabbitMQ: the base64-encoded Cuttlefish configuration.</p>
            description: <p>The description of the configuration.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.update_configuration_request.UpdateConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.update_configuration_response.UpdateConfigurationResponse"
        ]:
            import aws_sdk_mq._operations.mq.update_configuration

            output, http_response = (
                aws_sdk_mq._operations.mq.update_configuration.update_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.update_configuration_request.UpdateConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_id"] = configuration_id
        input_["data"] = data
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_user(
        self,
        broker_id: "aws_sdk_mq.types.__string.__string",
        username: "aws_sdk_mq.types.__string.__string",
        *,
        config_overrides: Optional[mqClientConfig] = None,
        console_access: Optional["aws_sdk_mq.types.__boolean.__boolean"] = None,
        groups: Optional["aws_sdk_mq.types.__list_of__string.__listOf__string"] = None,
        password: Optional["aws_sdk_mq.types.__string.__string"] = None,
        replication_user: Optional["aws_sdk_mq.types.__boolean.__boolean"] = None,
    ) -> "aws_sdk_mq.types.update_user_response.UpdateUserResponse":
        """<p>Updates the information for an ActiveMQ user.</p>

        Args:
            broker_id: <p>The unique ID that Amazon MQ generates for the broker.</p>
            console_access: <p>Enables access to the the ActiveMQ Web Console for the ActiveMQ user.</p>
            groups: <p>The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>
            password: <p>The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=).</p>
            username: <p>The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>
            replication_user: <p>Defines whether the user is intended for data replication.</p>

        Raises:
            aws_sdk_mq.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            aws_sdk_mq.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mq.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_mq.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_mq._operations.mq.update_user

            output, http_response = aws_sdk_mq._operations.mq.update_user.update_user(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mq.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["broker_id"] = broker_id
        if console_access is not None:
            input_["console_access"] = console_access
        if groups is not None:
            input_["groups"] = groups
        if password is not None:
            input_["password"] = password
        input_["username"] = username
        if replication_user is not None:
            input_["replication_user"] = replication_user

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
