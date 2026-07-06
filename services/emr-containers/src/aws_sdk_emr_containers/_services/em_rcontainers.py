"""Generated from Smithy shape ``com.amazonaws.emrcontainers#AwsChicagoWebService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_emr_containers._auth._signers
import aws_sdk_emr_containers._auth._sigv4
from aws_sdk_emr_containers._auth._identity import Credentials
from aws_sdk_emr_containers._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_emr_containers._auth._zapros_handler import AuthMiddleware
from aws_sdk_emr_containers._pagination import resolve_path as _resolve_path
from aws_sdk_emr_containers._services._aws_config import aws_config
from aws_sdk_emr_containers._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.acm_cert_arn
    import aws_sdk_emr_containers.types.boolean
    import aws_sdk_emr_containers.types.cancel_job_run_request
    import aws_sdk_emr_containers.types.cancel_job_run_response
    import aws_sdk_emr_containers.types.client_token
    import aws_sdk_emr_containers.types.configuration_overrides
    import aws_sdk_emr_containers.types.container_provider
    import aws_sdk_emr_containers.types.container_provider_type
    import aws_sdk_emr_containers.types.create_job_template_request
    import aws_sdk_emr_containers.types.create_job_template_response
    import aws_sdk_emr_containers.types.create_managed_endpoint_request
    import aws_sdk_emr_containers.types.create_managed_endpoint_response
    import aws_sdk_emr_containers.types.create_security_configuration_request
    import aws_sdk_emr_containers.types.create_security_configuration_response
    import aws_sdk_emr_containers.types.create_virtual_cluster_request
    import aws_sdk_emr_containers.types.create_virtual_cluster_response
    import aws_sdk_emr_containers.types.credential_type
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.delete_job_template_request
    import aws_sdk_emr_containers.types.delete_job_template_response
    import aws_sdk_emr_containers.types.delete_managed_endpoint_request
    import aws_sdk_emr_containers.types.delete_managed_endpoint_response
    import aws_sdk_emr_containers.types.delete_virtual_cluster_request
    import aws_sdk_emr_containers.types.delete_virtual_cluster_response
    import aws_sdk_emr_containers.types.describe_job_run_request
    import aws_sdk_emr_containers.types.describe_job_run_response
    import aws_sdk_emr_containers.types.describe_job_template_request
    import aws_sdk_emr_containers.types.describe_job_template_response
    import aws_sdk_emr_containers.types.describe_managed_endpoint_request
    import aws_sdk_emr_containers.types.describe_managed_endpoint_response
    import aws_sdk_emr_containers.types.describe_security_configuration_request
    import aws_sdk_emr_containers.types.describe_security_configuration_response
    import aws_sdk_emr_containers.types.describe_virtual_cluster_request
    import aws_sdk_emr_containers.types.describe_virtual_cluster_response
    import aws_sdk_emr_containers.types.endpoint
    import aws_sdk_emr_containers.types.endpoint_states
    import aws_sdk_emr_containers.types.endpoint_type
    import aws_sdk_emr_containers.types.endpoint_types
    import aws_sdk_emr_containers.types.get_managed_endpoint_session_credentials_request
    import aws_sdk_emr_containers.types.get_managed_endpoint_session_credentials_response
    import aws_sdk_emr_containers.types.iam_role_arn
    import aws_sdk_emr_containers.types.java_integer
    import aws_sdk_emr_containers.types.job_driver
    import aws_sdk_emr_containers.types.job_run
    import aws_sdk_emr_containers.types.job_run_states
    import aws_sdk_emr_containers.types.job_template
    import aws_sdk_emr_containers.types.job_template_data
    import aws_sdk_emr_containers.types.kms_key_arn
    import aws_sdk_emr_containers.types.list_job_runs_request
    import aws_sdk_emr_containers.types.list_job_runs_response
    import aws_sdk_emr_containers.types.list_job_templates_request
    import aws_sdk_emr_containers.types.list_job_templates_response
    import aws_sdk_emr_containers.types.list_managed_endpoints_request
    import aws_sdk_emr_containers.types.list_managed_endpoints_response
    import aws_sdk_emr_containers.types.list_security_configurations_request
    import aws_sdk_emr_containers.types.list_security_configurations_response
    import aws_sdk_emr_containers.types.list_tags_for_resource_request
    import aws_sdk_emr_containers.types.list_tags_for_resource_response
    import aws_sdk_emr_containers.types.list_virtual_clusters_request
    import aws_sdk_emr_containers.types.list_virtual_clusters_response
    import aws_sdk_emr_containers.types.log_context
    import aws_sdk_emr_containers.types.next_token
    import aws_sdk_emr_containers.types.release_label
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.retry_policy_configuration
    import aws_sdk_emr_containers.types.rsi_arn
    import aws_sdk_emr_containers.types.security_configuration
    import aws_sdk_emr_containers.types.security_configuration_data
    import aws_sdk_emr_containers.types.start_job_run_request
    import aws_sdk_emr_containers.types.start_job_run_response
    import aws_sdk_emr_containers.types.string1024
    import aws_sdk_emr_containers.types.string2048
    import aws_sdk_emr_containers.types.tag_key_list
    import aws_sdk_emr_containers.types.tag_map
    import aws_sdk_emr_containers.types.tag_resource_request
    import aws_sdk_emr_containers.types.tag_resource_response
    import aws_sdk_emr_containers.types.template_parameter_input_map
    import aws_sdk_emr_containers.types.untag_resource_request
    import aws_sdk_emr_containers.types.untag_resource_response
    import aws_sdk_emr_containers.types.virtual_cluster
    import aws_sdk_emr_containers.types.virtual_cluster_states


class EMRcontainersClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class EMRcontainersClient:
    """A client for the ``EMRcontainers`` service.

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
        self._config = EMRcontainersClientConfig(
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
        self, config_overrides: Optional[EMRcontainersClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EMRcontainersClientConfig = config_overrides or {}
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

    def cancel_job_run(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.cancel_job_run_response.CancelJobRunResponse":
        """<p>Cancels a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.</p>

        Args:
            id: <p>The ID of the job run to cancel.</p>
            virtual_cluster_id: <p>The ID of the virtual cluster for which the job run will be canceled.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.cancel_job_run_request.CancelJobRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.cancel_job_run_response.CancelJobRunResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.cancel_job_run

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.cancel_job_run.cancel_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.cancel_job_run_request.CancelJobRunRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["virtual_cluster_id"] = virtual_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_job_template(
        self,
        name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString",
        client_token: "aws_sdk_emr_containers.types.client_token.ClientToken",
        job_template_data: "aws_sdk_emr_containers.types.job_template_data.JobTemplateData",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        tags: Optional["aws_sdk_emr_containers.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional[
            "aws_sdk_emr_containers.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.create_job_template_response.CreateJobTemplateResponse":
        """<p>Creates a job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.</p>

        Args:
            name: <p>The specified name of the job template.</p>
            client_token: <p>The client token of the job template.</p>
            job_template_data: <p>The job template data which holds values of StartJobRun API request.</p>
            tags: <p>The tags that are associated with the job template.</p>
            kms_key_arn: <p>The KMS key ARN used to encrypt the job template.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.create_job_template_request.CreateJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.create_job_template_response.CreateJobTemplateResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.create_job_template

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.create_job_template.create_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.create_job_template_request.CreateJobTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["client_token"] = client_token
        input_["job_template_data"] = job_template_data
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_managed_endpoint(
        self,
        name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString",
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        type: "aws_sdk_emr_containers.types.endpoint_type.EndpointType",
        release_label: "aws_sdk_emr_containers.types.release_label.ReleaseLabel",
        execution_role_arn: "aws_sdk_emr_containers.types.iam_role_arn.IAMRoleArn",
        client_token: "aws_sdk_emr_containers.types.client_token.ClientToken",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        certificate_arn: Optional[
            "aws_sdk_emr_containers.types.acm_cert_arn.ACMCertArn"
        ] = None,
        configuration_overrides: Optional[
            "aws_sdk_emr_containers.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
        tags: Optional["aws_sdk_emr_containers.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_emr_containers.types.create_managed_endpoint_response.CreateManagedEndpointResponse":
        """<p>Creates a managed endpoint. A managed endpoint is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that Amazon EMR Studio can communicate with your virtual cluster.</p>

        Args:
            name: <p>The name of the managed endpoint.</p>
            virtual_cluster_id: <p>The ID of the virtual cluster for which a managed endpoint is created.</p>
            type: <p>The type of the managed endpoint.</p>
            release_label: <p>The Amazon EMR release version.</p>
            execution_role_arn: <p>The ARN of the execution role.</p>
            certificate_arn: <p>The certificate ARN provided by users for the managed endpoint. This field is under deprecation and will be removed in future releases.</p>
            configuration_overrides: <p>The configuration settings that will be used to override existing configurations.</p>
            client_token: <p>The client idempotency token for this create call.</p>
            tags: <p>The tags of the managed endpoint. </p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.create_managed_endpoint_request.CreateManagedEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.create_managed_endpoint_response.CreateManagedEndpointResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.create_managed_endpoint

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.create_managed_endpoint.create_managed_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.create_managed_endpoint_request.CreateManagedEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["virtual_cluster_id"] = virtual_cluster_id
        input_["type"] = type
        input_["release_label"] = release_label
        input_["execution_role_arn"] = execution_role_arn
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_security_configuration(
        self,
        client_token: "aws_sdk_emr_containers.types.client_token.ClientToken",
        name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString",
        security_configuration_data: "aws_sdk_emr_containers.types.security_configuration_data.SecurityConfigurationData",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        container_provider: Optional[
            "aws_sdk_emr_containers.types.container_provider.ContainerProvider"
        ] = None,
        tags: Optional["aws_sdk_emr_containers.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_emr_containers.types.create_security_configuration_response.CreateSecurityConfigurationResponse":
        """<p>Creates a security configuration. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.</p>

        Args:
            client_token: <p>The client idempotency token to use when creating the security configuration.</p>
            name: <p>The name of the security configuration.</p>
            container_provider: <p>The container provider associated with the security configuration.</p>
            security_configuration_data: <p>Security configuration input for the request.</p>
            tags: <p>The tags to add to the security configuration.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.create_security_configuration_request.CreateSecurityConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.create_security_configuration_response.CreateSecurityConfigurationResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.create_security_configuration

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.create_security_configuration.create_security_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.create_security_configuration_request.CreateSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["client_token"] = client_token
        input_["name"] = name
        if container_provider is not None:
            input_["container_provider"] = container_provider
        input_["security_configuration_data"] = security_configuration_data
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_virtual_cluster(
        self,
        name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString",
        container_provider: "aws_sdk_emr_containers.types.container_provider.ContainerProvider",
        client_token: "aws_sdk_emr_containers.types.client_token.ClientToken",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        tags: Optional["aws_sdk_emr_containers.types.tag_map.TagMap"] = None,
        security_configuration_id: Optional[
            "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.create_virtual_cluster_response.CreateVirtualClusterResponse":
        """<p>Creates a virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.</p>

        Args:
            name: <p>The specified name of the virtual cluster.</p>
            container_provider: <p>The container provider of the virtual cluster.</p>
            client_token: <p>The client token of the virtual cluster.</p>
            tags: <p>The tags assigned to the virtual cluster.</p>
            security_configuration_id: <p>The ID of the security configuration.</p>

        Raises:
            aws_sdk_emr_containers.errors.eks_request_throttled_exception.EKSRequestThrottledException: <p>The request exceeded the Amazon EKS API operation limits.</p>
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.create_virtual_cluster_request.CreateVirtualClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.create_virtual_cluster_response.CreateVirtualClusterResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.create_virtual_cluster

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.create_virtual_cluster.create_virtual_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.create_virtual_cluster_request.CreateVirtualClusterRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["container_provider"] = container_provider
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if security_configuration_id is not None:
            input_["security_configuration_id"] = security_configuration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_job_template(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.delete_job_template_response.DeleteJobTemplateResponse":
        """<p>Deletes a job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.</p>

        Args:
            id: <p>The ID of the job template that will be deleted.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.delete_job_template_request.DeleteJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.delete_job_template_response.DeleteJobTemplateResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.delete_job_template

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.delete_job_template.delete_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.delete_job_template_request.DeleteJobTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_managed_endpoint(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.delete_managed_endpoint_response.DeleteManagedEndpointResponse":
        """<p>Deletes a managed endpoint. A managed endpoint is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that Amazon EMR Studio can communicate with your virtual cluster.</p>

        Args:
            id: <p>The ID of the managed endpoint.</p>
            virtual_cluster_id: <p>The ID of the endpoint's virtual cluster.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.delete_managed_endpoint_request.DeleteManagedEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.delete_managed_endpoint_response.DeleteManagedEndpointResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.delete_managed_endpoint

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.delete_managed_endpoint.delete_managed_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.delete_managed_endpoint_request.DeleteManagedEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["virtual_cluster_id"] = virtual_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_virtual_cluster(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.delete_virtual_cluster_response.DeleteVirtualClusterResponse":
        """<p>Deletes a virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.</p>

        Args:
            id: <p>The ID of the virtual cluster that will be deleted.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.delete_virtual_cluster_request.DeleteVirtualClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.delete_virtual_cluster_response.DeleteVirtualClusterResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.delete_virtual_cluster

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.delete_virtual_cluster.delete_virtual_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.delete_virtual_cluster_request.DeleteVirtualClusterRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_job_run(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> (
        "aws_sdk_emr_containers.types.describe_job_run_response.DescribeJobRunResponse"
    ):
        """<p>Displays detailed information about a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.</p>

        Args:
            id: <p>The ID of the job run request. </p>
            virtual_cluster_id: <p>The ID of the virtual cluster for which the job run is submitted.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.describe_job_run_request.DescribeJobRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.describe_job_run_response.DescribeJobRunResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_job_run

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_job_run.describe_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.describe_job_run_request.DescribeJobRunRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["virtual_cluster_id"] = virtual_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_job_template(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.describe_job_template_response.DescribeJobTemplateResponse":
        """<p>Displays detailed information about a specified job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.</p>

        Args:
            id: <p>The ID of the job template that will be described.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.describe_job_template_request.DescribeJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.describe_job_template_response.DescribeJobTemplateResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_job_template

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_job_template.describe_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.describe_job_template_request.DescribeJobTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_managed_endpoint(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.describe_managed_endpoint_response.DescribeManagedEndpointResponse":
        """<p>Displays detailed information about a managed endpoint. A managed endpoint is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that Amazon EMR Studio can communicate with your virtual cluster.</p>

        Args:
            id: <p>This output displays ID of the managed endpoint.</p>
            virtual_cluster_id: <p>The ID of the endpoint's virtual cluster.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.describe_managed_endpoint_request.DescribeManagedEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.describe_managed_endpoint_response.DescribeManagedEndpointResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_managed_endpoint

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_managed_endpoint.describe_managed_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.describe_managed_endpoint_request.DescribeManagedEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["virtual_cluster_id"] = virtual_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_security_configuration(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.describe_security_configuration_response.DescribeSecurityConfigurationResponse":
        """<p>Displays detailed information about a specified security configuration. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.</p>

        Args:
            id: <p>The ID of the security configuration.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.describe_security_configuration_request.DescribeSecurityConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.describe_security_configuration_response.DescribeSecurityConfigurationResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_security_configuration

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_security_configuration.describe_security_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.describe_security_configuration_request.DescribeSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_virtual_cluster(
        self,
        id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.describe_virtual_cluster_response.DescribeVirtualClusterResponse":
        """<p>Displays detailed information about a specified virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.</p>

        Args:
            id: <p>The ID of the virtual cluster that will be described.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.describe_virtual_cluster_request.DescribeVirtualClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.describe_virtual_cluster_response.DescribeVirtualClusterResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_virtual_cluster

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.describe_virtual_cluster.describe_virtual_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.describe_virtual_cluster_request.DescribeVirtualClusterRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_managed_endpoint_session_credentials(
        self,
        endpoint_identifier: "aws_sdk_emr_containers.types.string2048.String2048",
        virtual_cluster_identifier: "aws_sdk_emr_containers.types.string2048.String2048",
        execution_role_arn: "aws_sdk_emr_containers.types.iam_role_arn.IAMRoleArn",
        credential_type: "aws_sdk_emr_containers.types.credential_type.CredentialType",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        duration_in_seconds: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        log_context: Optional[
            "aws_sdk_emr_containers.types.log_context.LogContext"
        ] = None,
        client_token: Optional[
            "aws_sdk_emr_containers.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.get_managed_endpoint_session_credentials_response.GetManagedEndpointSessionCredentialsResponse":
        """<p>Generate a session token to connect to a managed endpoint. </p>

        Args:
            endpoint_identifier: <p>The ARN of the managed endpoint for which the request is submitted. </p>
            virtual_cluster_identifier: <p>The ARN of the Virtual Cluster which the Managed Endpoint belongs to. </p>
            execution_role_arn: <p>The IAM Execution Role ARN that will be used by the job run. </p>
            credential_type: <p>Type of the token requested. Currently supported and default value of this field is “TOKEN.”</p>
            duration_in_seconds: <p>Duration in seconds for which the session token is valid. The default duration is 15 minutes and the maximum is 12 hours.</p>
            log_context: <p>String identifier used to separate sections of the execution logs uploaded to S3.</p>
            client_token: <p>The client idempotency token of the job run request.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.request_throttled_exception.RequestThrottledException: <p>The request throttled.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.get_managed_endpoint_session_credentials_request.GetManagedEndpointSessionCredentialsRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.get_managed_endpoint_session_credentials_response.GetManagedEndpointSessionCredentialsResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.get_managed_endpoint_session_credentials

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.get_managed_endpoint_session_credentials.get_managed_endpoint_session_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.get_managed_endpoint_session_credentials_request.GetManagedEndpointSessionCredentialsRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_identifier"] = endpoint_identifier
        input_["virtual_cluster_identifier"] = virtual_cluster_identifier
        input_["execution_role_arn"] = execution_role_arn
        input_["credential_type"] = credential_type
        if duration_in_seconds is not None:
            input_["duration_in_seconds"] = duration_in_seconds
        if log_context is not None:
            input_["log_context"] = log_context
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_job_runs(
        self,
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        name: Optional[
            "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
        ] = None,
        states: Optional[
            "aws_sdk_emr_containers.types.job_run_states.JobRunStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.list_job_runs_response.ListJobRunsResponse":
        """<p>Lists job runs based on a set of parameters. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.</p>

        Args:
            virtual_cluster_id: <p>The ID of the virtual cluster for which to list the job run. </p>
            created_before: <p>The date and time before which the job runs were submitted.</p>
            created_after: <p>The date and time after which the job runs were submitted.</p>
            name: <p>The name of the job run.</p>
            states: <p>The states of the job run.</p>
            max_results: <p>The maximum number of job runs that can be listed.</p>
            next_token: <p>The token for the next set of job runs to return.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.list_job_runs_request.ListJobRunsRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.list_job_runs_response.ListJobRunsResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.list_job_runs

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.list_job_runs.list_job_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.list_job_runs_request.ListJobRunsRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_cluster_id"] = virtual_cluster_id
        if created_before is not None:
            input_["created_before"] = created_before
        if created_after is not None:
            input_["created_after"] = created_after
        if name is not None:
            input_["name"] = name
        if states is not None:
            input_["states"] = states
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

    def iter_list_job_runs(
        self,
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        name: Optional[
            "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
        ] = None,
        states: Optional[
            "aws_sdk_emr_containers.types.job_run_states.JobRunStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_emr_containers.types.job_run.JobRun]":
        _token = next_token
        while True:
            _response = self.list_job_runs(
                virtual_cluster_id,
                config_overrides=config_overrides,
                created_before=created_before,
                created_after=created_after,
                name=name,
                states=states,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_job_templates(
        self,
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.list_job_templates_response.ListJobTemplatesResponse":
        """<p>Lists job templates based on a set of parameters. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.</p>

        Args:
            created_after: <p>The date and time after which the job templates were created.</p>
            created_before: <p> The date and time before which the job templates were created.</p>
            max_results: <p> The maximum number of job templates that can be listed.</p>
            next_token: <p> The token for the next set of job templates to return.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.list_job_templates_request.ListJobTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.list_job_templates_response.ListJobTemplatesResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.list_job_templates

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.list_job_templates.list_job_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.list_job_templates_request.ListJobTemplatesRequest = {}  # type: ignore[typeddict-item]
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
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

    def iter_list_job_templates(
        self,
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_emr_containers.types.job_template.JobTemplate]":
        _token = next_token
        while True:
            _response = self.list_job_templates(
                config_overrides=config_overrides,
                created_after=created_after,
                created_before=created_before,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_managed_endpoints(
        self,
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        types: Optional[
            "aws_sdk_emr_containers.types.endpoint_types.EndpointTypes"
        ] = None,
        states: Optional[
            "aws_sdk_emr_containers.types.endpoint_states.EndpointStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.list_managed_endpoints_response.ListManagedEndpointsResponse":
        """<p>Lists managed endpoints based on a set of parameters. A managed endpoint is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that Amazon EMR Studio can communicate with your virtual cluster.</p>

        Args:
            virtual_cluster_id: <p>The ID of the virtual cluster.</p>
            created_before: <p>The date and time before which the endpoints are created.</p>
            created_after: <p> The date and time after which the endpoints are created.</p>
            types: <p>The types of the managed endpoints.</p>
            states: <p>The states of the managed endpoints.</p>
            max_results: <p>The maximum number of managed endpoints that can be listed.</p>
            next_token: <p> The token for the next set of managed endpoints to return. </p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.list_managed_endpoints_request.ListManagedEndpointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.list_managed_endpoints_response.ListManagedEndpointsResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.list_managed_endpoints

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.list_managed_endpoints.list_managed_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.list_managed_endpoints_request.ListManagedEndpointsRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_cluster_id"] = virtual_cluster_id
        if created_before is not None:
            input_["created_before"] = created_before
        if created_after is not None:
            input_["created_after"] = created_after
        if types is not None:
            input_["types"] = types
        if states is not None:
            input_["states"] = states
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

    def iter_list_managed_endpoints(
        self,
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        types: Optional[
            "aws_sdk_emr_containers.types.endpoint_types.EndpointTypes"
        ] = None,
        states: Optional[
            "aws_sdk_emr_containers.types.endpoint_states.EndpointStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_emr_containers.types.endpoint.Endpoint]":
        _token = next_token
        while True:
            _response = self.list_managed_endpoints(
                virtual_cluster_id,
                config_overrides=config_overrides,
                created_before=created_before,
                created_after=created_after,
                types=types,
                states=states,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_security_configurations(
        self,
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.list_security_configurations_response.ListSecurityConfigurationsResponse":
        """<p>Lists security configurations based on a set of parameters. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.</p>

        Args:
            created_after: <p>The date and time after which the security configuration was created.</p>
            created_before: <p>The date and time before which the security configuration was created.</p>
            max_results: <p>The maximum number of security configurations the operation can list.</p>
            next_token: <p>The token for the next set of security configurations to return.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.list_security_configurations_request.ListSecurityConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.list_security_configurations_response.ListSecurityConfigurationsResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.list_security_configurations

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.list_security_configurations.list_security_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.list_security_configurations_request.ListSecurityConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
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

    def iter_list_security_configurations(
        self,
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_emr_containers.types.security_configuration.SecurityConfiguration]":
        _token = next_token
        while True:
            _response = self.list_security_configurations(
                config_overrides=config_overrides,
                created_after=created_after,
                created_before=created_before,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("security_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_emr_containers.types.rsi_arn.RsiArn",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to the resources.</p>

        Args:
            resource_arn: <p>The ARN of tagged resources.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_virtual_clusters(
        self,
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        container_provider_id: Optional[
            "aws_sdk_emr_containers.types.string1024.String1024"
        ] = None,
        container_provider_type: Optional[
            "aws_sdk_emr_containers.types.container_provider_type.ContainerProviderType"
        ] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        states: Optional[
            "aws_sdk_emr_containers.types.virtual_cluster_states.VirtualClusterStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
        eks_access_entry_integrated: Optional[
            "aws_sdk_emr_containers.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.list_virtual_clusters_response.ListVirtualClustersResponse":
        """<p>Lists information about the specified virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.</p>

        Args:
            container_provider_id: <p>The container provider ID of the virtual cluster.</p>
            container_provider_type: <p>The container provider type of the virtual cluster. Amazon EKS is the only supported type as of now.</p>
            created_after: <p>The date and time after which the virtual clusters are created.</p>
            created_before: <p>The date and time before which the virtual clusters are created.</p>
            states: <p>The states of the requested virtual clusters.</p>
            max_results: <p>The maximum number of virtual clusters that can be listed.</p>
            next_token: <p>The token for the next set of virtual clusters to return. </p>
            eks_access_entry_integrated: <p>Optional Boolean that specifies whether the operation should return the virtual clusters that have the access entry integration enabled or disabled. If not specified, the operation returns all applicable virtual clusters.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.list_virtual_clusters_request.ListVirtualClustersRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.list_virtual_clusters_response.ListVirtualClustersResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.list_virtual_clusters

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.list_virtual_clusters.list_virtual_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.list_virtual_clusters_request.ListVirtualClustersRequest = {}  # type: ignore[typeddict-item]
        if container_provider_id is not None:
            input_["container_provider_id"] = container_provider_id
        if container_provider_type is not None:
            input_["container_provider_type"] = container_provider_type
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
        if states is not None:
            input_["states"] = states
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if eks_access_entry_integrated is not None:
            input_["eks_access_entry_integrated"] = eks_access_entry_integrated

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_virtual_clusters(
        self,
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        container_provider_id: Optional[
            "aws_sdk_emr_containers.types.string1024.String1024"
        ] = None,
        container_provider_type: Optional[
            "aws_sdk_emr_containers.types.container_provider_type.ContainerProviderType"
        ] = None,
        created_after: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        created_before: Optional["aws_sdk_emr_containers.types.date.Date"] = None,
        states: Optional[
            "aws_sdk_emr_containers.types.virtual_cluster_states.VirtualClusterStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_emr_containers.types.java_integer.JavaInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_emr_containers.types.next_token.NextToken"
        ] = None,
        eks_access_entry_integrated: Optional[
            "aws_sdk_emr_containers.types.boolean.Boolean"
        ] = None,
    ) -> "Iterator[aws_sdk_emr_containers.types.virtual_cluster.VirtualCluster]":
        _token = next_token
        while True:
            _response = self.list_virtual_clusters(
                config_overrides=config_overrides,
                container_provider_id=container_provider_id,
                container_provider_type=container_provider_type,
                created_after=created_after,
                created_before=created_before,
                states=states,
                max_results=max_results,
                next_token=_token,
                eks_access_entry_integrated=eks_access_entry_integrated,
            )
            _page = _resolve_path(_response, ("virtual_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_job_run(
        self,
        virtual_cluster_id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString",
        client_token: "aws_sdk_emr_containers.types.client_token.ClientToken",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
        name: Optional[
            "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_emr_containers.types.iam_role_arn.IAMRoleArn"
        ] = None,
        release_label: Optional[
            "aws_sdk_emr_containers.types.release_label.ReleaseLabel"
        ] = None,
        job_driver: Optional[
            "aws_sdk_emr_containers.types.job_driver.JobDriver"
        ] = None,
        configuration_overrides: Optional[
            "aws_sdk_emr_containers.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
        tags: Optional["aws_sdk_emr_containers.types.tag_map.TagMap"] = None,
        job_template_id: Optional[
            "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
        ] = None,
        job_template_parameters: Optional[
            "aws_sdk_emr_containers.types.template_parameter_input_map.TemplateParameterInputMap"
        ] = None,
        retry_policy_configuration: Optional[
            "aws_sdk_emr_containers.types.retry_policy_configuration.RetryPolicyConfiguration"
        ] = None,
    ) -> "aws_sdk_emr_containers.types.start_job_run_response.StartJobRunResponse":
        """<p>Starts a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.</p>

        Args:
            name: <p>The name of the job run.</p>
            virtual_cluster_id: <p>The virtual cluster ID for which the job run request is submitted.</p>
            client_token: <p>The client idempotency token of the job run request. </p>
            execution_role_arn: <p>The execution role ARN for the job run.</p>
            release_label: <p>The Amazon EMR release version to use for the job run.</p>
            job_driver: <p>The job driver for the job run.</p>
            configuration_overrides: <p>The configuration overrides for the job run.</p>
            tags: <p>The tags assigned to job runs.</p>
            job_template_id: <p>The job template ID to be used to start the job run.</p>
            job_template_parameters: <p>The values of job template parameters to start a job run.</p>
            retry_policy_configuration: <p>The retry policy configuration for the job run.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.start_job_run_request.StartJobRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.start_job_run_response.StartJobRunResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.start_job_run

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.start_job_run.start_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.start_job_run_request.StartJobRunRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        input_["virtual_cluster_id"] = virtual_cluster_id
        input_["client_token"] = client_token
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if release_label is not None:
            input_["release_label"] = release_label
        if job_driver is not None:
            input_["job_driver"] = job_driver
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if job_template_id is not None:
            input_["job_template_id"] = job_template_id
        if job_template_parameters is not None:
            input_["job_template_parameters"] = job_template_parameters
        if retry_policy_configuration is not None:
            input_["retry_policy_configuration"] = retry_policy_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_emr_containers.types.rsi_arn.RsiArn",
        tags: "aws_sdk_emr_containers.types.tag_map.TagMap",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns tags to resources. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize your Amazon Web Services resources by attributes such as purpose, owner, or environment. When you have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned to it. For example, you can define a set of tags for your Amazon EMR on EKS clusters to help you track each cluster's owner and stack level. We recommend that you devise a consistent set of tag keys for each resource type. You can then search and filter the resources based on the tags that you add.</p>

        Args:
            resource_arn: <p>The ARN of resources.</p>
            tags: <p>The tags assigned to resources.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.tag_resource

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_emr_containers.types.rsi_arn.RsiArn",
        tag_keys: "aws_sdk_emr_containers.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[EMRcontainersClientConfig] = None,
    ) -> "aws_sdk_emr_containers.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from resources.</p>

        Args:
            resource_arn: <p>The ARN of resources.</p>
            tag_keys: <p>The tag keys of the resources.</p>

        Raises:
            aws_sdk_emr_containers.errors.internal_server_exception.InternalServerException: <p>This is an internal server exception.</p>
            aws_sdk_emr_containers.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            aws_sdk_emr_containers.errors.validation_exception.ValidationException: <p>There are invalid parameters in the client request.</p>
            aws_sdk_emr_containers.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_containers.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_containers.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_emr_containers._operations.aws_chicago_web_service.untag_resource

            output, http_response = (
                aws_sdk_emr_containers._operations.aws_chicago_web_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_containers.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
