"""Generated from Smithy shape ``com.amazonaws.odb#Odb``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_odb._auth._signers
import aws_sdk_odb._auth._sigv4
from aws_sdk_odb._auth._identity import Credentials
from aws_sdk_odb._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_odb._auth._zapros_handler import AuthMiddleware
from aws_sdk_odb._pagination import resolve_path as _resolve_path
from aws_sdk_odb._resources.odb.autonomous_database_backup_resource import (
    AutonomousDatabaseBackupResource,
)
from aws_sdk_odb._resources.odb.autonomous_database_resource import (
    AutonomousDatabaseResource,
)
from aws_sdk_odb._resources.odb.cloud_autonomous_vm_cluster_resource import (
    CloudAutonomousVmClusterResource,
)
from aws_sdk_odb._resources.odb.cloud_exadata_infrastructure_resource import (
    CloudExadataInfrastructureResource,
)
from aws_sdk_odb._resources.odb.cloud_vm_cluster_resource import CloudVmClusterResource
from aws_sdk_odb._resources.odb.db_node_resource import DbNodeResource
from aws_sdk_odb._resources.odb.exadb_vm_cluster_resource import ExadbVmClusterResource
from aws_sdk_odb._resources.odb.exascale_db_storage_vault_resource import (
    ExascaleDbStorageVaultResource,
)
from aws_sdk_odb._resources.odb.exascale_vm_cluster_resource import (
    ExascaleVmClusterResource,
)
from aws_sdk_odb._resources.odb.odb_network_resource import OdbNetworkResource
from aws_sdk_odb._resources.odb.odb_peering_connection_resource import (
    OdbPeeringConnectionResource,
)
from aws_sdk_odb._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_odb.types.accept_marketplace_registration_input
    import aws_sdk_odb.types.accept_marketplace_registration_output
    import aws_sdk_odb.types.arn
    import aws_sdk_odb.types.associate_iam_role_to_resource_input
    import aws_sdk_odb.types.associate_iam_role_to_resource_output
    import aws_sdk_odb.types.autonomous_database_character_set_summary
    import aws_sdk_odb.types.autonomous_database_version_summary
    import aws_sdk_odb.types.character_set_type
    import aws_sdk_odb.types.db_system_shape_summary
    import aws_sdk_odb.types.db_workload
    import aws_sdk_odb.types.disassociate_iam_role_from_resource_input
    import aws_sdk_odb.types.disassociate_iam_role_from_resource_output
    import aws_sdk_odb.types.get_oci_onboarding_status_input
    import aws_sdk_odb.types.get_oci_onboarding_status_output
    import aws_sdk_odb.types.gi_version_summary
    import aws_sdk_odb.types.initialize_service_input
    import aws_sdk_odb.types.initialize_service_output
    import aws_sdk_odb.types.list_autonomous_database_character_sets_input
    import aws_sdk_odb.types.list_autonomous_database_character_sets_output
    import aws_sdk_odb.types.list_autonomous_database_versions_input
    import aws_sdk_odb.types.list_autonomous_database_versions_output
    import aws_sdk_odb.types.list_db_system_shapes_input
    import aws_sdk_odb.types.list_db_system_shapes_output
    import aws_sdk_odb.types.list_gi_versions_input
    import aws_sdk_odb.types.list_gi_versions_output
    import aws_sdk_odb.types.list_system_versions_input
    import aws_sdk_odb.types.list_system_versions_output
    import aws_sdk_odb.types.list_tags_for_resource_request
    import aws_sdk_odb.types.list_tags_for_resource_response
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.role_arn
    import aws_sdk_odb.types.supported_aws_integration
    import aws_sdk_odb.types.system_version_summary
    import aws_sdk_odb.types.tag_keys
    import aws_sdk_odb.types.tag_resource_request
    import aws_sdk_odb.types.tag_resource_response
    import aws_sdk_odb.types.untag_resource_request
    import aws_sdk_odb.types.untag_resource_response


class odbClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class odbClient:
    """A client for the ``odb`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = odbClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )
        # resources
        self.autonomous_database_backup_resource = AutonomousDatabaseBackupResource(
            self
        )
        self.autonomous_database_resource = AutonomousDatabaseResource(self)
        self.cloud_autonomous_vm_cluster_resource = CloudAutonomousVmClusterResource(
            self
        )
        self.cloud_exadata_infrastructure_resource = CloudExadataInfrastructureResource(
            self
        )
        self.cloud_vm_cluster_resource = CloudVmClusterResource(self)
        self.db_node_resource = DbNodeResource(self)
        self.exadb_vm_cluster_resource = ExadbVmClusterResource(self)
        self.exascale_db_storage_vault_resource = ExascaleDbStorageVaultResource(self)
        self.exascale_vm_cluster_resource = ExascaleVmClusterResource(self)
        self.odb_network_resource = OdbNetworkResource(self)
        self.odb_peering_connection_resource = OdbPeeringConnectionResource(self)

    def operation_options(
        self, config_overrides: Optional[odbClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: odbClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def accept_marketplace_registration(
        self,
        marketplace_registration_token: str,
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.accept_marketplace_registration_output.AcceptMarketplaceRegistrationOutput":
        """<p>Registers the Amazon Web Services Marketplace token for your Amazon Web Services account to activate your Oracle Database@Amazon Web Services subscription.</p>

        Args:
            marketplace_registration_token: <p>The registration token that's generated by Amazon Web Services Marketplace and sent to Oracle Database@Amazon Web Services.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.accept_marketplace_registration_input.AcceptMarketplaceRegistrationInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.accept_marketplace_registration_output.AcceptMarketplaceRegistrationOutput"
        ]:
            import aws_sdk_odb._operations.odb.accept_marketplace_registration

            output, http_response = (
                aws_sdk_odb._operations.odb.accept_marketplace_registration.accept_marketplace_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.accept_marketplace_registration_input.AcceptMarketplaceRegistrationInput = {}  # type: ignore[typeddict-item]
        input_["marketplace_registration_token"] = marketplace_registration_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_iam_role_to_resource(
        self,
        iam_role_arn: "aws_sdk_odb.types.role_arn.RoleArn",
        aws_integration: "aws_sdk_odb.types.supported_aws_integration.SupportedAwsIntegration",
        resource_arn: "aws_sdk_odb.types.arn.Arn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.associate_iam_role_to_resource_output.AssociateIamRoleToResourceOutput":
        """<p>Associates an Amazon Web Services Identity and Access Management (IAM) service role with a specified resource to enable Amazon Web Services service integration.</p>

        Args:
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role to associate with the resource.</p>
            aws_integration: <p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role association.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the target resource to associate with the Amazon Web Services Identity and Access Management (IAM) service role.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.associate_iam_role_to_resource_input.AssociateIamRoleToResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.associate_iam_role_to_resource_output.AssociateIamRoleToResourceOutput"
        ]:
            import aws_sdk_odb._operations.odb.associate_iam_role_to_resource

            output, http_response = (
                aws_sdk_odb._operations.odb.associate_iam_role_to_resource.associate_iam_role_to_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.associate_iam_role_to_resource_input.AssociateIamRoleToResourceInput = {}  # type: ignore[typeddict-item]
        input_["iam_role_arn"] = iam_role_arn
        input_["aws_integration"] = aws_integration
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_iam_role_from_resource(
        self,
        iam_role_arn: "aws_sdk_odb.types.role_arn.RoleArn",
        aws_integration: "aws_sdk_odb.types.supported_aws_integration.SupportedAwsIntegration",
        resource_arn: "aws_sdk_odb.types.arn.Arn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.disassociate_iam_role_from_resource_output.DisassociateIamRoleFromResourceOutput":
        """<p>Disassociates an Amazon Web Services Identity and Access Management (IAM) service role from a specified resource to disable Amazon Web Services service integration.</p>

        Args:
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role to disassociate from the resource.</p>
            aws_integration: <p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role disassociation.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the target resource to disassociate from the Amazon Web Services Identity and Access Management (IAM) service role.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.disassociate_iam_role_from_resource_input.DisassociateIamRoleFromResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.disassociate_iam_role_from_resource_output.DisassociateIamRoleFromResourceOutput"
        ]:
            import aws_sdk_odb._operations.odb.disassociate_iam_role_from_resource

            output, http_response = (
                aws_sdk_odb._operations.odb.disassociate_iam_role_from_resource.disassociate_iam_role_from_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.disassociate_iam_role_from_resource_input.DisassociateIamRoleFromResourceInput = {}  # type: ignore[typeddict-item]
        input_["iam_role_arn"] = iam_role_arn
        input_["aws_integration"] = aws_integration
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_oci_onboarding_status(
        self, *, config_overrides: Optional[odbClientConfig] = None
    ) -> "aws_sdk_odb.types.get_oci_onboarding_status_output.GetOciOnboardingStatusOutput":
        """<p>Returns the tenancy activation link and onboarding status for your Amazon Web Services account.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_oci_onboarding_status_input.GetOciOnboardingStatusInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.get_oci_onboarding_status_output.GetOciOnboardingStatusOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_oci_onboarding_status

            output, http_response = (
                aws_sdk_odb._operations.odb.get_oci_onboarding_status.get_oci_onboarding_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_oci_onboarding_status_input.GetOciOnboardingStatusInput = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def initialize_service(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        oci_identity_domain: Optional[bool] = None,
    ) -> "aws_sdk_odb.types.initialize_service_output.InitializeServiceOutput":
        """<p>Initializes the ODB service for the first time in an account.</p>

        Args:
            oci_identity_domain: <p>The Oracle Cloud Infrastructure (OCI) identity domain configuration for service initialization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.initialize_service_input.InitializeServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.initialize_service_output.InitializeServiceOutput"
        ]:
            import aws_sdk_odb._operations.odb.initialize_service

            output, http_response = (
                aws_sdk_odb._operations.odb.initialize_service.initialize_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.initialize_service_input.InitializeServiceInput = {}  # type: ignore[typeddict-item]
        if oci_identity_domain is not None:
            input_["oci_identity_domain"] = oci_identity_domain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_autonomous_database_character_sets(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        character_set_type: Optional[
            "aws_sdk_odb.types.character_set_type.characterSetType"
        ] = None,
    ) -> "aws_sdk_odb.types.list_autonomous_database_character_sets_output.ListAutonomousDatabaseCharacterSetsOutput":
        """<p>Lists the available character sets for Autonomous Databases.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            character_set_type: <p>The type of character set to return results for, either the database character set or the national character set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_autonomous_database_character_sets_input.ListAutonomousDatabaseCharacterSetsInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_autonomous_database_character_sets_output.ListAutonomousDatabaseCharacterSetsOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_autonomous_database_character_sets

            output, http_response = (
                aws_sdk_odb._operations.odb.list_autonomous_database_character_sets.list_autonomous_database_character_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_autonomous_database_character_sets_input.ListAutonomousDatabaseCharacterSetsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if character_set_type is not None:
            input_["character_set_type"] = character_set_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_autonomous_database_character_sets(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        character_set_type: Optional[
            "aws_sdk_odb.types.character_set_type.characterSetType"
        ] = None,
    ) -> "Iterator[aws_sdk_odb.types.autonomous_database_character_set_summary.AutonomousDatabaseCharacterSetSummary]":
        _token = next_token
        while True:
            _response = self.list_autonomous_database_character_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                character_set_type=character_set_type,
            )
            _page = _resolve_path(_response, ("autonomous_database_character_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_autonomous_database_versions(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        db_workload: Optional["aws_sdk_odb.types.db_workload.DbWorkload"] = None,
    ) -> "aws_sdk_odb.types.list_autonomous_database_versions_output.ListAutonomousDatabaseVersionsOutput":
        """<p>Lists the available Oracle Database software versions for Autonomous Databases.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            db_workload: <p>The intended use of the Autonomous Database to return versions for, such as transaction processing, data warehouse, JSON database, or APEX.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_autonomous_database_versions_input.ListAutonomousDatabaseVersionsInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_autonomous_database_versions_output.ListAutonomousDatabaseVersionsOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_autonomous_database_versions

            output, http_response = (
                aws_sdk_odb._operations.odb.list_autonomous_database_versions.list_autonomous_database_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_autonomous_database_versions_input.ListAutonomousDatabaseVersionsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if db_workload is not None:
            input_["db_workload"] = db_workload

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_autonomous_database_versions(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        db_workload: Optional["aws_sdk_odb.types.db_workload.DbWorkload"] = None,
    ) -> "Iterator[aws_sdk_odb.types.autonomous_database_version_summary.AutonomousDatabaseVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_autonomous_database_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                db_workload=db_workload,
            )
            _page = _resolve_path(_response, ("autonomous_database_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_db_system_shapes(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_db_system_shapes_output.ListDbSystemShapesOutput":
        """<p>Returns information about the shapes that are available for an Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            availability_zone: <p>The logical name of the AZ, for example, us-east-1a. This name varies depending on the account.</p>
            availability_zone_id: <p>The physical ID of the AZ, for example, use1-az4. This ID persists across accounts.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_db_system_shapes_input.ListDbSystemShapesInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_db_system_shapes_output.ListDbSystemShapesOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_db_system_shapes

            output, http_response = (
                aws_sdk_odb._operations.odb.list_db_system_shapes.list_db_system_shapes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_db_system_shapes_input.ListDbSystemShapesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_db_system_shapes(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
    ) -> "Iterator[aws_sdk_odb.types.db_system_shape_summary.DbSystemShapeSummary]":
        _token = next_token
        while True:
            _response = self.list_db_system_shapes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
            )
            _page = _resolve_path(_response, ("db_system_shapes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_gi_versions(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_gi_versions_output.ListGiVersionsOutput":
        """<p>Returns information about Oracle Grid Infrastructure (GI) software versions that are available for a VM cluster for the specified shape.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            shape: <p>The shape to return GI versions for. For a list of valid shapes, use the <code>ListDbSystemShapes</code> operation..</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_gi_versions_input.ListGiVersionsInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_gi_versions_output.ListGiVersionsOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_gi_versions

            output, http_response = (
                aws_sdk_odb._operations.odb.list_gi_versions.list_gi_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_gi_versions_input.ListGiVersionsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if shape is not None:
            input_["shape"] = shape

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_gi_versions(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape: Optional[str] = None,
    ) -> "Iterator[aws_sdk_odb.types.gi_version_summary.GiVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_gi_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                shape=shape,
            )
            _page = _resolve_path(_response, ("gi_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_system_versions(
        self,
        gi_version: str,
        shape: str,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_system_versions_output.ListSystemVersionsOutput":
        """<p>Returns information about the system versions that are available for a VM cluster for the specified <code>giVersion</code> and <code>shape</code>.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            gi_version: <p>The software version of the Exadata Grid Infrastructure (GI).</p>
            shape: <p>The Exadata hardware system model.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_system_versions_input.ListSystemVersionsInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_system_versions_output.ListSystemVersionsOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_system_versions

            output, http_response = (
                aws_sdk_odb._operations.odb.list_system_versions.list_system_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_system_versions_input.ListSystemVersionsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["gi_version"] = gi_version
        input_["shape"] = shape

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_system_versions(
        self,
        gi_version: str,
        shape: str,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[aws_sdk_odb.types.system_version_summary.SystemVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_system_versions(
                gi_version,
                shape,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("system_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_odb.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> (
        "aws_sdk_odb.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Returns information about the tags applied to this resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_odb._operations.odb.list_tags_for_resource

            output, http_response = (
                aws_sdk_odb._operations.odb.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_odb.types.resource_arn.ResourceArn",
        tags: "aws_sdk_odb.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.tag_resource_response.TagResourceResponse":
        """<p>Applies tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to apply tags to.</p>
            tags: <p>The list of tags to apply to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_odb._operations.odb.tag_resource

            output, http_response = (
                aws_sdk_odb._operations.odb.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_odb.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_odb.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The names (keys) of the tags to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_odb._operations.odb.untag_resource

            output, http_response = (
                aws_sdk_odb._operations.odb.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_odb.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
