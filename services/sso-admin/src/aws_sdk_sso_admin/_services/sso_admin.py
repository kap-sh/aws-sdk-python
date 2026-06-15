"""Generated from Smithy shape ``com.amazonaws.ssoadmin#SWBExternalService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_sso_admin._auth._signers
import aws_sdk_sso_admin._auth._sigv4
from aws_sdk_sso_admin._auth._identity import Credentials
from aws_sdk_sso_admin._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sso_admin._auth._zapros_handler import AuthMiddleware
from aws_sdk_sso_admin._pagination import resolve_path as _resolve_path
from aws_sdk_sso_admin._resources.swb_external_service.application_access_scope_resource import (
    ApplicationAccessScopeResource,
)
from aws_sdk_sso_admin._resources.swb_external_service.application_authentication_method_resource import (
    ApplicationAuthenticationMethodResource,
)
from aws_sdk_sso_admin._resources.swb_external_service.application_grant_resource import (
    ApplicationGrantResource,
)
from aws_sdk_sso_admin._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment
    import aws_sdk_sso_admin.types.account_assignment_for_principal
    import aws_sdk_sso_admin.types.account_assignment_operation_status_metadata
    import aws_sdk_sso_admin.types.account_id
    import aws_sdk_sso_admin.types.add_region_request
    import aws_sdk_sso_admin.types.add_region_response
    import aws_sdk_sso_admin.types.application
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.application_assignment
    import aws_sdk_sso_admin.types.application_assignment_for_principal
    import aws_sdk_sso_admin.types.application_name_type
    import aws_sdk_sso_admin.types.application_provider
    import aws_sdk_sso_admin.types.application_provider_arn
    import aws_sdk_sso_admin.types.application_status
    import aws_sdk_sso_admin.types.assignment_required
    import aws_sdk_sso_admin.types.attach_customer_managed_policy_reference_to_permission_set_request
    import aws_sdk_sso_admin.types.attach_customer_managed_policy_reference_to_permission_set_response
    import aws_sdk_sso_admin.types.attach_managed_policy_to_permission_set_request
    import aws_sdk_sso_admin.types.attach_managed_policy_to_permission_set_response
    import aws_sdk_sso_admin.types.attached_managed_policy
    import aws_sdk_sso_admin.types.client_token
    import aws_sdk_sso_admin.types.create_account_assignment_request
    import aws_sdk_sso_admin.types.create_account_assignment_response
    import aws_sdk_sso_admin.types.create_application_assignment_request
    import aws_sdk_sso_admin.types.create_application_assignment_response
    import aws_sdk_sso_admin.types.create_application_request
    import aws_sdk_sso_admin.types.create_application_response
    import aws_sdk_sso_admin.types.create_instance_access_control_attribute_configuration_request
    import aws_sdk_sso_admin.types.create_instance_access_control_attribute_configuration_response
    import aws_sdk_sso_admin.types.create_instance_request
    import aws_sdk_sso_admin.types.create_instance_response
    import aws_sdk_sso_admin.types.create_permission_set_request
    import aws_sdk_sso_admin.types.create_permission_set_response
    import aws_sdk_sso_admin.types.create_trusted_token_issuer_request
    import aws_sdk_sso_admin.types.create_trusted_token_issuer_response
    import aws_sdk_sso_admin.types.customer_managed_policy_reference
    import aws_sdk_sso_admin.types.delete_account_assignment_request
    import aws_sdk_sso_admin.types.delete_account_assignment_response
    import aws_sdk_sso_admin.types.delete_application_assignment_request
    import aws_sdk_sso_admin.types.delete_application_assignment_response
    import aws_sdk_sso_admin.types.delete_application_request
    import aws_sdk_sso_admin.types.delete_application_response
    import aws_sdk_sso_admin.types.delete_inline_policy_from_permission_set_request
    import aws_sdk_sso_admin.types.delete_inline_policy_from_permission_set_response
    import aws_sdk_sso_admin.types.delete_instance_access_control_attribute_configuration_request
    import aws_sdk_sso_admin.types.delete_instance_access_control_attribute_configuration_response
    import aws_sdk_sso_admin.types.delete_instance_request
    import aws_sdk_sso_admin.types.delete_instance_response
    import aws_sdk_sso_admin.types.delete_permission_set_request
    import aws_sdk_sso_admin.types.delete_permission_set_response
    import aws_sdk_sso_admin.types.delete_permissions_boundary_from_permission_set_request
    import aws_sdk_sso_admin.types.delete_permissions_boundary_from_permission_set_response
    import aws_sdk_sso_admin.types.delete_trusted_token_issuer_request
    import aws_sdk_sso_admin.types.delete_trusted_token_issuer_response
    import aws_sdk_sso_admin.types.describe_account_assignment_creation_status_request
    import aws_sdk_sso_admin.types.describe_account_assignment_creation_status_response
    import aws_sdk_sso_admin.types.describe_account_assignment_deletion_status_request
    import aws_sdk_sso_admin.types.describe_account_assignment_deletion_status_response
    import aws_sdk_sso_admin.types.describe_application_assignment_request
    import aws_sdk_sso_admin.types.describe_application_assignment_response
    import aws_sdk_sso_admin.types.describe_application_provider_request
    import aws_sdk_sso_admin.types.describe_application_provider_response
    import aws_sdk_sso_admin.types.describe_application_request
    import aws_sdk_sso_admin.types.describe_application_response
    import aws_sdk_sso_admin.types.describe_instance_access_control_attribute_configuration_request
    import aws_sdk_sso_admin.types.describe_instance_access_control_attribute_configuration_response
    import aws_sdk_sso_admin.types.describe_instance_request
    import aws_sdk_sso_admin.types.describe_instance_response
    import aws_sdk_sso_admin.types.describe_permission_set_provisioning_status_request
    import aws_sdk_sso_admin.types.describe_permission_set_provisioning_status_response
    import aws_sdk_sso_admin.types.describe_permission_set_request
    import aws_sdk_sso_admin.types.describe_permission_set_response
    import aws_sdk_sso_admin.types.describe_region_request
    import aws_sdk_sso_admin.types.describe_region_response
    import aws_sdk_sso_admin.types.describe_trusted_token_issuer_request
    import aws_sdk_sso_admin.types.describe_trusted_token_issuer_response
    import aws_sdk_sso_admin.types.description
    import aws_sdk_sso_admin.types.detach_customer_managed_policy_reference_from_permission_set_request
    import aws_sdk_sso_admin.types.detach_customer_managed_policy_reference_from_permission_set_response
    import aws_sdk_sso_admin.types.detach_managed_policy_from_permission_set_request
    import aws_sdk_sso_admin.types.detach_managed_policy_from_permission_set_response
    import aws_sdk_sso_admin.types.duration
    import aws_sdk_sso_admin.types.encryption_configuration
    import aws_sdk_sso_admin.types.get_application_assignment_configuration_request
    import aws_sdk_sso_admin.types.get_application_assignment_configuration_response
    import aws_sdk_sso_admin.types.get_application_session_configuration_request
    import aws_sdk_sso_admin.types.get_application_session_configuration_response
    import aws_sdk_sso_admin.types.get_inline_policy_for_permission_set_request
    import aws_sdk_sso_admin.types.get_inline_policy_for_permission_set_response
    import aws_sdk_sso_admin.types.get_permissions_boundary_for_permission_set_request
    import aws_sdk_sso_admin.types.get_permissions_boundary_for_permission_set_response
    import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.instance_metadata
    import aws_sdk_sso_admin.types.list_account_assignment_creation_status_request
    import aws_sdk_sso_admin.types.list_account_assignment_creation_status_response
    import aws_sdk_sso_admin.types.list_account_assignment_deletion_status_request
    import aws_sdk_sso_admin.types.list_account_assignment_deletion_status_response
    import aws_sdk_sso_admin.types.list_account_assignments_filter
    import aws_sdk_sso_admin.types.list_account_assignments_for_principal_request
    import aws_sdk_sso_admin.types.list_account_assignments_for_principal_response
    import aws_sdk_sso_admin.types.list_account_assignments_request
    import aws_sdk_sso_admin.types.list_account_assignments_response
    import aws_sdk_sso_admin.types.list_accounts_for_provisioned_permission_set_request
    import aws_sdk_sso_admin.types.list_accounts_for_provisioned_permission_set_response
    import aws_sdk_sso_admin.types.list_application_assignments_filter
    import aws_sdk_sso_admin.types.list_application_assignments_for_principal_request
    import aws_sdk_sso_admin.types.list_application_assignments_for_principal_response
    import aws_sdk_sso_admin.types.list_application_assignments_request
    import aws_sdk_sso_admin.types.list_application_assignments_response
    import aws_sdk_sso_admin.types.list_application_providers_request
    import aws_sdk_sso_admin.types.list_application_providers_response
    import aws_sdk_sso_admin.types.list_applications_filter
    import aws_sdk_sso_admin.types.list_applications_request
    import aws_sdk_sso_admin.types.list_applications_response
    import aws_sdk_sso_admin.types.list_customer_managed_policy_references_in_permission_set_request
    import aws_sdk_sso_admin.types.list_customer_managed_policy_references_in_permission_set_response
    import aws_sdk_sso_admin.types.list_instances_request
    import aws_sdk_sso_admin.types.list_instances_response
    import aws_sdk_sso_admin.types.list_managed_policies_in_permission_set_request
    import aws_sdk_sso_admin.types.list_managed_policies_in_permission_set_response
    import aws_sdk_sso_admin.types.list_permission_set_provisioning_status_request
    import aws_sdk_sso_admin.types.list_permission_set_provisioning_status_response
    import aws_sdk_sso_admin.types.list_permission_sets_provisioned_to_account_request
    import aws_sdk_sso_admin.types.list_permission_sets_provisioned_to_account_response
    import aws_sdk_sso_admin.types.list_permission_sets_request
    import aws_sdk_sso_admin.types.list_permission_sets_response
    import aws_sdk_sso_admin.types.list_regions_request
    import aws_sdk_sso_admin.types.list_regions_response
    import aws_sdk_sso_admin.types.list_tags_for_resource_request
    import aws_sdk_sso_admin.types.list_tags_for_resource_response
    import aws_sdk_sso_admin.types.list_trusted_token_issuers_request
    import aws_sdk_sso_admin.types.list_trusted_token_issuers_response
    import aws_sdk_sso_admin.types.managed_policy_arn
    import aws_sdk_sso_admin.types.max_results
    import aws_sdk_sso_admin.types.name_type
    import aws_sdk_sso_admin.types.operation_status_filter
    import aws_sdk_sso_admin.types.permission_set_arn
    import aws_sdk_sso_admin.types.permission_set_description
    import aws_sdk_sso_admin.types.permission_set_name
    import aws_sdk_sso_admin.types.permission_set_policy_document
    import aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata
    import aws_sdk_sso_admin.types.permissions_boundary
    import aws_sdk_sso_admin.types.portal_options
    import aws_sdk_sso_admin.types.principal_id
    import aws_sdk_sso_admin.types.principal_type
    import aws_sdk_sso_admin.types.provision_permission_set_request
    import aws_sdk_sso_admin.types.provision_permission_set_response
    import aws_sdk_sso_admin.types.provision_target_type
    import aws_sdk_sso_admin.types.provisioning_status
    import aws_sdk_sso_admin.types.put_application_assignment_configuration_request
    import aws_sdk_sso_admin.types.put_application_assignment_configuration_response
    import aws_sdk_sso_admin.types.put_application_session_configuration_request
    import aws_sdk_sso_admin.types.put_application_session_configuration_response
    import aws_sdk_sso_admin.types.put_inline_policy_to_permission_set_request
    import aws_sdk_sso_admin.types.put_inline_policy_to_permission_set_response
    import aws_sdk_sso_admin.types.put_permissions_boundary_to_permission_set_request
    import aws_sdk_sso_admin.types.put_permissions_boundary_to_permission_set_response
    import aws_sdk_sso_admin.types.region_metadata
    import aws_sdk_sso_admin.types.region_name
    import aws_sdk_sso_admin.types.relay_state
    import aws_sdk_sso_admin.types.remove_region_request
    import aws_sdk_sso_admin.types.remove_region_response
    import aws_sdk_sso_admin.types.tag
    import aws_sdk_sso_admin.types.tag_key_list
    import aws_sdk_sso_admin.types.tag_list
    import aws_sdk_sso_admin.types.tag_resource_request
    import aws_sdk_sso_admin.types.tag_resource_response
    import aws_sdk_sso_admin.types.taggable_resource_arn
    import aws_sdk_sso_admin.types.target_id
    import aws_sdk_sso_admin.types.target_type
    import aws_sdk_sso_admin.types.token
    import aws_sdk_sso_admin.types.trusted_token_issuer_arn
    import aws_sdk_sso_admin.types.trusted_token_issuer_configuration
    import aws_sdk_sso_admin.types.trusted_token_issuer_metadata
    import aws_sdk_sso_admin.types.trusted_token_issuer_name
    import aws_sdk_sso_admin.types.trusted_token_issuer_type
    import aws_sdk_sso_admin.types.trusted_token_issuer_update_configuration
    import aws_sdk_sso_admin.types.untag_resource_request
    import aws_sdk_sso_admin.types.untag_resource_response
    import aws_sdk_sso_admin.types.update_application_portal_options
    import aws_sdk_sso_admin.types.update_application_request
    import aws_sdk_sso_admin.types.update_application_response
    import aws_sdk_sso_admin.types.update_instance_access_control_attribute_configuration_request
    import aws_sdk_sso_admin.types.update_instance_access_control_attribute_configuration_response
    import aws_sdk_sso_admin.types.update_instance_request
    import aws_sdk_sso_admin.types.update_instance_response
    import aws_sdk_sso_admin.types.update_permission_set_request
    import aws_sdk_sso_admin.types.update_permission_set_response
    import aws_sdk_sso_admin.types.update_trusted_token_issuer_request
    import aws_sdk_sso_admin.types.update_trusted_token_issuer_response
    import aws_sdk_sso_admin.types.user_background_session_application_status
    import aws_sdk_sso_admin.types.uu_id


class SSOAdminClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class SSOAdminClient:
    """A client for the ``SSOAdmin`` service.

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
        self._config = SSOAdminClientConfig(
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
        self.application_access_scope_resource = ApplicationAccessScopeResource(self)
        self.application_authentication_method_resource = (
            ApplicationAuthenticationMethodResource(self)
        )
        self.application_grant_resource = ApplicationGrantResource(self)

    def operation_options(
        self, config_overrides: Optional[SSOAdminClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SSOAdminClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    def add_region(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        region_name: "aws_sdk_sso_admin.types.region_name.RegionName",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.add_region_response.AddRegionResponse":
        r"""<p>Adds a Region to an IAM Identity Center instance. This operation initiates an asynchronous workflow to replicate the IAM Identity Center instance to the target Region. The Region status is set to ADDING at first and changes to ACTIVE when the workflow completes.</p> <p>To use this operation, your IAM Identity Center instance and the target Region must meet the requirements described in the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html#multi-region-prerequisites\">IAM Identity Center User Guide</a>. </p> <p>The following actions are related to <code>AddRegion</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html\">RemoveRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html\">DescribeRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html\">ListRegions</a> </p> </li> </ul>

        Args:
            instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to replicate to the target Region.</p>
            region_name: <p>The name of the Amazon Web Services Region to add to the IAM Identity Center instance. The Region name must be 1-32 characters long and follow the pattern of Amazon Web Services Region names (for example, us-east-1).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.add_region_request.AddRegionRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.add_region_response.AddRegionResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.add_region

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.add_region.add_region(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.add_region_request.AddRegionRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["region_name"] = region_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def attach_customer_managed_policy_reference_to_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        customer_managed_policy_reference: "aws_sdk_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.attach_customer_managed_policy_reference_to_permission_set_response.AttachCustomerManagedPolicyReferenceToPermissionSetResponse":
        """<p>Attaches the specified customer managed policy to the specified <a>PermissionSet</a>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>
            permission_set_arn: <p>The ARN of the <code>PermissionSet</code>.</p>
            customer_managed_policy_reference: <p>Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each Amazon Web Services account where you want to deploy your permission set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.attach_customer_managed_policy_reference_to_permission_set_request.AttachCustomerManagedPolicyReferenceToPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.attach_customer_managed_policy_reference_to_permission_set_response.AttachCustomerManagedPolicyReferenceToPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.attach_customer_managed_policy_reference_to_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.attach_customer_managed_policy_reference_to_permission_set.attach_customer_managed_policy_reference_to_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.attach_customer_managed_policy_reference_to_permission_set_request.AttachCustomerManagedPolicyReferenceToPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        input_["customer_managed_policy_reference"] = customer_managed_policy_reference

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def attach_managed_policy_to_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        managed_policy_arn: "aws_sdk_sso_admin.types.managed_policy_arn.ManagedPolicyArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.attach_managed_policy_to_permission_set_response.AttachManagedPolicyToPermissionSetResponse":
        r"""<p>Attaches an Amazon Web Services managed policy ARN to a permission set.</p> <note> <p>If the permission set is already referenced by one or more account assignments, you will need to call <code> <a>ProvisionPermissionSet</a> </code> after this operation. Calling <code>ProvisionPermissionSet</code> applies the corresponding IAM policy updates to all assigned accounts.</p> </note>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the <a>PermissionSet</a> that the managed policy should be attached to.</p>
            managed_policy_arn: <p>The Amazon Web Services managed policy ARN to be attached to a permission set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.attach_managed_policy_to_permission_set_request.AttachManagedPolicyToPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.attach_managed_policy_to_permission_set_response.AttachManagedPolicyToPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.attach_managed_policy_to_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.attach_managed_policy_to_permission_set.attach_managed_policy_to_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.attach_managed_policy_to_permission_set_request.AttachManagedPolicyToPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        input_["managed_policy_arn"] = managed_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_account_assignment(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        target_id: "aws_sdk_sso_admin.types.target_id.TargetId",
        target_type: "aws_sdk_sso_admin.types.target_type.TargetType",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.create_account_assignment_response.CreateAccountAssignmentResponse":
        r"""<p>Assigns access to a principal for a specified Amazon Web Services account using a specified permission set.</p> <note> <p>The term <i>principal</i> here refers to a user or group that is defined in IAM Identity Center.</p> </note> <note> <p>As part of a successful <code>CreateAccountAssignment</code> call, the specified permission set will automatically be provisioned to the account in the form of an IAM policy. That policy is attached to the IAM role created in IAM Identity Center. If the permission set is subsequently updated, the corresponding IAM policies attached to roles in your accounts will not be updated automatically. In this case, you must call <code> <a>ProvisionPermissionSet</a> </code> to make these updates.</p> </note> <note> <p> After a successful response, call <code>DescribeAccountAssignmentCreationStatus</code> to describe the status of an assignment creation request. </p> </note>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            target_id: <p>TargetID is an Amazon Web Services account identifier, (For example, 123456789012).</p>
            target_type: <p>The entity type for which the assignment will be created.</p>
            permission_set_arn: <p>The ARN of the permission set that the admin wants to grant the principal access to.</p>
            principal_type: <p>The entity type for which the assignment will be created.</p>
            principal_id: <p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href=\"/singlesignon/latest/IdentityStoreAPIReference/welcome.html\">IAM Identity Center Identity Store API Reference</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_account_assignment_request.CreateAccountAssignmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_account_assignment_response.CreateAccountAssignmentResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_account_assignment

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_account_assignment.create_account_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_account_assignment_request.CreateAccountAssignmentRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["target_id"] = target_id
        input_["target_type"] = target_type
        input_["permission_set_arn"] = permission_set_arn
        input_["principal_type"] = principal_type
        input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_application(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        application_provider_arn: "aws_sdk_sso_admin.types.application_provider_arn.ApplicationProviderArn",
        name: "aws_sdk_sso_admin.types.application_name_type.ApplicationNameType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        description: Optional["aws_sdk_sso_admin.types.description.Description"] = None,
        portal_options: Optional[
            "aws_sdk_sso_admin.types.portal_options.PortalOptions"
        ] = None,
        tags: Optional["aws_sdk_sso_admin.types.tag_list.TagList"] = None,
        status: Optional[
            "aws_sdk_sso_admin.types.application_status.ApplicationStatus"
        ] = None,
        client_token: Optional[
            "aws_sdk_sso_admin.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_sso_admin.types.create_application_response.CreateApplicationResponse"
    ):
        r"""<p>Creates an OAuth 2.0 customer managed application in IAM Identity Center for the given application provider.</p> <note> <p>This API does not support creating SAML 2.0 customer managed applications or Amazon Web Services managed applications. To learn how to create an Amazon Web Services managed application, see the application user guide. You can create a SAML 2.0 customer managed application in the Amazon Web Services Management Console only. See <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html\">Setting up customer managed SAML 2.0 applications</a>. For more information on these application types, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html\">Amazon Web Services managed applications</a>.</p> </note>

        Args:
            instance_arn: <p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            application_provider_arn: <p>The ARN of the application provider under which the operation will run.</p>
            name: <p>The name of the .</p>
            description: <p>The description of the .</p>
            portal_options: <p>A structure that describes the options for the portal associated with an application.</p>
            tags: <p>Specifies tags to be attached to the application.</p>
            status: <p>Specifies whether the application is enabled or disabled.</p>
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_application_response.CreateApplicationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_application

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["application_provider_arn"] = application_provider_arn
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if portal_options is not None:
            input_["portal_options"] = portal_options
        if tags is not None:
            input_["tags"] = tags
        if status is not None:
            input_["status"] = status
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_application_assignment(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.create_application_assignment_response.CreateApplicationAssignmentResponse":
        r"""<p>Grant application access to a user or group.</p>

        Args:
            application_arn: <p>The ARN of the application for which the assignment is created.</p>
            principal_id: <p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html\">IAM Identity Center Identity Store API Reference</a>.</p>
            principal_type: <p>The entity type for which the assignment will be created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_application_assignment_request.CreateApplicationAssignmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_application_assignment_response.CreateApplicationAssignmentResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_application_assignment

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_application_assignment.create_application_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_application_assignment_request.CreateApplicationAssignmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["principal_id"] = principal_id
        input_["principal_type"] = principal_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_instance(
        self,
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        name: Optional["aws_sdk_sso_admin.types.name_type.NameType"] = None,
        client_token: Optional[
            "aws_sdk_sso_admin.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_sso_admin.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_sso_admin.types.create_instance_response.CreateInstanceResponse":
        r"""<p>Creates an instance of IAM Identity Center for a standalone Amazon Web Services account that is not managed by Organizations or a member Amazon Web Services account in an organization. You can create only one instance per account and across all Amazon Web Services Regions.</p> <p>The CreateInstance request is rejected if the following apply: </p> <ul> <li> <p>The instance is created within the organization management account.</p> </li> <li> <p>An instance already exists in the same account.</p> </li> </ul>

        Args:
            name: <p>The name of the instance of IAM Identity Center.</p>
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>Specifies tags to be attached to the instance of IAM Identity Center.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_instance_request.CreateInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_instance_response.CreateInstanceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_instance

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_instance.create_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_instance_request.CreateInstanceRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_instance_access_control_attribute_configuration(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        instance_access_control_attribute_configuration: "aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.InstanceAccessControlAttributeConfiguration",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.create_instance_access_control_attribute_configuration_response.CreateInstanceAccessControlAttributeConfigurationResponse":
        r"""<p>Enables the attributes-based access control (ABAC) feature for the specified IAM Identity Center instance. You can also specify new attributes to add to your ABAC configuration during the enabling process. For more information about ABAC, see <a href=\"/singlesignon/latest/userguide/abac.html\">Attribute-Based Access Control</a> in the <i>IAM Identity Center User Guide</i>.</p> <note> <p>After a successful response, call <code>DescribeInstanceAccessControlAttributeConfiguration</code> to validate that <code>InstanceAccessControlAttributeConfiguration</code> was created.</p> </note>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>
            instance_access_control_attribute_configuration: <p>Specifies the IAM Identity Center identity store attributes to add to your ABAC configuration. When using an external identity provider as an identity source, you can pass attributes through the SAML assertion. Doing so provides an alternative to configuring attributes from the IAM Identity Center identity store. If a SAML assertion passes any of these attributes, IAM Identity Center will replace the attribute value with the value from the IAM Identity Center identity store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_instance_access_control_attribute_configuration_request.CreateInstanceAccessControlAttributeConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_instance_access_control_attribute_configuration_response.CreateInstanceAccessControlAttributeConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_instance_access_control_attribute_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_instance_access_control_attribute_configuration.create_instance_access_control_attribute_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_instance_access_control_attribute_configuration_request.CreateInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["instance_access_control_attribute_configuration"] = (
            instance_access_control_attribute_configuration
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_permission_set(
        self,
        name: "aws_sdk_sso_admin.types.permission_set_name.PermissionSetName",
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        description: Optional[
            "aws_sdk_sso_admin.types.permission_set_description.PermissionSetDescription"
        ] = None,
        session_duration: Optional["aws_sdk_sso_admin.types.duration.Duration"] = None,
        relay_state: Optional["aws_sdk_sso_admin.types.relay_state.RelayState"] = None,
        tags: Optional["aws_sdk_sso_admin.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_sso_admin.types.create_permission_set_response.CreatePermissionSetResponse":
        r"""<p>Creates a permission set within a specified IAM Identity Center instance.</p> <note> <p>To grant users and groups access to Amazon Web Services account resources, use <code> <a>CreateAccountAssignment</a> </code>.</p> </note>

        Args:
            name: <p>The name of the <a>PermissionSet</a>.</p>
            description: <p>The description of the <a>PermissionSet</a>.</p>
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            session_duration: <p>The length of time that the application user sessions are valid in the ISO-8601 standard.</p>
            relay_state: <p>Used to redirect users within the application during the federation authentication process.</p>
            tags: <p>The tags to attach to the new <a>PermissionSet</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_permission_set_request.CreatePermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_permission_set_response.CreatePermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_permission_set.create_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_permission_set_request.CreatePermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["instance_arn"] = instance_arn
        if session_duration is not None:
            input_["session_duration"] = session_duration
        if relay_state is not None:
            input_["relay_state"] = relay_state
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_trusted_token_issuer(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        name: "aws_sdk_sso_admin.types.trusted_token_issuer_name.TrustedTokenIssuerName",
        trusted_token_issuer_type: "aws_sdk_sso_admin.types.trusted_token_issuer_type.TrustedTokenIssuerType",
        trusted_token_issuer_configuration: "aws_sdk_sso_admin.types.trusted_token_issuer_configuration.TrustedTokenIssuerConfiguration",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        client_token: Optional[
            "aws_sdk_sso_admin.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_sso_admin.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_sso_admin.types.create_trusted_token_issuer_response.CreateTrustedTokenIssuerResponse":
        r"""<p>Creates a connection to a trusted token issuer in an instance of IAM Identity Center. A trusted token issuer enables trusted identity propagation to be used with applications that authenticate outside of Amazon Web Services.</p> <p>This trusted token issuer describes an external identity provider (IdP) that can generate claims or assertions in the form of access tokens for a user. Applications enabled for IAM Identity Center can use these tokens for authentication. </p>

        Args:
            instance_arn: <p>Specifies the ARN of the instance of IAM Identity Center to contain the new trusted token issuer configuration.</p>
            name: <p>Specifies the name of the new trusted token issuer configuration.</p>
            trusted_token_issuer_type: <p>Specifies the type of the new trusted token issuer.</p>
            trusted_token_issuer_configuration: <p>Specifies settings that apply to the new trusted token issuer configuration. The settings that are available depend on what <code>TrustedTokenIssuerType</code> you specify.</p>
            client_token: <p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>Specifies tags to be attached to the new trusted token issuer configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.create_trusted_token_issuer_request.CreateTrustedTokenIssuerRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.create_trusted_token_issuer_response.CreateTrustedTokenIssuerResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.create_trusted_token_issuer

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.create_trusted_token_issuer.create_trusted_token_issuer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.create_trusted_token_issuer_request.CreateTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["name"] = name
        input_["trusted_token_issuer_type"] = trusted_token_issuer_type
        input_["trusted_token_issuer_configuration"] = (
            trusted_token_issuer_configuration
        )
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_account_assignment(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        target_id: "aws_sdk_sso_admin.types.target_id.TargetId",
        target_type: "aws_sdk_sso_admin.types.target_type.TargetType",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_account_assignment_response.DeleteAccountAssignmentResponse":
        r"""<p>Deletes a principal's access from a specified Amazon Web Services account using a specified permission set.</p> <note> <p>After a successful response, call <code>DescribeAccountAssignmentDeletionStatus</code> to describe the status of an assignment deletion request.</p> </note>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            target_id: <p>TargetID is an Amazon Web Services account identifier, (For example, 123456789012).</p>
            target_type: <p>The entity type for which the assignment will be deleted.</p>
            permission_set_arn: <p>The ARN of the permission set that will be used to remove access.</p>
            principal_type: <p>The entity type for which the assignment will be deleted.</p>
            principal_id: <p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href=\"/singlesignon/latest/IdentityStoreAPIReference/welcome.html\">IAM Identity Center Identity Store API Reference</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_account_assignment_request.DeleteAccountAssignmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_account_assignment_response.DeleteAccountAssignmentResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_account_assignment

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_account_assignment.delete_account_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_account_assignment_request.DeleteAccountAssignmentRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["target_id"] = target_id
        input_["target_type"] = target_type
        input_["permission_set_arn"] = permission_set_arn
        input_["principal_type"] = principal_type
        input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_application(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> (
        "aws_sdk_sso_admin.types.delete_application_response.DeleteApplicationResponse"
    ):
        r"""<p>Deletes the association with the application. The connected service resource still exists.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_application

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_application_assignment(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_application_assignment_response.DeleteApplicationAssignmentResponse":
        r"""<p>Revoke application access to an application by deleting application assignments for a user or group.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            principal_id: <p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html\">IAM Identity Center Identity Store API Reference</a>.</p>
            principal_type: <p>The entity type for which the assignment will be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_application_assignment_request.DeleteApplicationAssignmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_application_assignment_response.DeleteApplicationAssignmentResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_application_assignment

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_application_assignment.delete_application_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_application_assignment_request.DeleteApplicationAssignmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["principal_id"] = principal_id
        input_["principal_type"] = principal_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_inline_policy_from_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_inline_policy_from_permission_set_response.DeleteInlinePolicyFromPermissionSetResponse":
        r"""<p>Deletes the inline policy from a specified permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set that will be used to remove access.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_inline_policy_from_permission_set_request.DeleteInlinePolicyFromPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_inline_policy_from_permission_set_response.DeleteInlinePolicyFromPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_inline_policy_from_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_inline_policy_from_permission_set.delete_inline_policy_from_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_inline_policy_from_permission_set_request.DeleteInlinePolicyFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_instance(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_instance_response.DeleteInstanceResponse":
        """<p>Deletes the instance of IAM Identity Center. Only the account that owns the instance can call this API. Neither the delegated administrator nor member account can delete the organization instance, but those roles can delete their own instance.</p>

        Args:
            instance_arn: <p>The ARN of the instance of IAM Identity Center under which the operation will run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_instance_request.DeleteInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_instance_response.DeleteInstanceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_instance

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_instance.delete_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_instance_request.DeleteInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_instance_access_control_attribute_configuration(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_instance_access_control_attribute_configuration_response.DeleteInstanceAccessControlAttributeConfigurationResponse":
        r"""<p>Disables the attributes-based access control (ABAC) feature for the specified IAM Identity Center instance and deletes all of the attribute mappings that have been configured. Once deleted, any attributes that are received from an identity source and any custom attributes you have previously configured will not be passed. For more information about ABAC, see <a href=\"/singlesignon/latest/userguide/abac.html\">Attribute-Based Access Control</a> in the <i>IAM Identity Center User Guide</i>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_instance_access_control_attribute_configuration_request.DeleteInstanceAccessControlAttributeConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_instance_access_control_attribute_configuration_response.DeleteInstanceAccessControlAttributeConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_instance_access_control_attribute_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_instance_access_control_attribute_configuration.delete_instance_access_control_attribute_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_instance_access_control_attribute_configuration_request.DeleteInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_permissions_boundary_from_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_permissions_boundary_from_permission_set_response.DeletePermissionsBoundaryFromPermissionSetResponse":
        """<p>Deletes the permissions boundary from a specified <a>PermissionSet</a>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>
            permission_set_arn: <p>The ARN of the <code>PermissionSet</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_permissions_boundary_from_permission_set_request.DeletePermissionsBoundaryFromPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_permissions_boundary_from_permission_set_response.DeletePermissionsBoundaryFromPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_permissions_boundary_from_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_permissions_boundary_from_permission_set.delete_permissions_boundary_from_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_permissions_boundary_from_permission_set_request.DeletePermissionsBoundaryFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_permission_set_response.DeletePermissionSetResponse":
        r"""<p>Deletes the specified permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set that should be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_permission_set_request.DeletePermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_permission_set_response.DeletePermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_permission_set.delete_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_permission_set_request.DeletePermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_trusted_token_issuer(
        self,
        trusted_token_issuer_arn: "aws_sdk_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.delete_trusted_token_issuer_response.DeleteTrustedTokenIssuerResponse":
        """<p>Deletes a trusted token issuer configuration from an instance of IAM Identity Center.</p> <note> <p>Deleting this trusted token issuer configuration will cause users to lose access to any applications that are configured to use the trusted token issuer.</p> </note>

        Args:
            trusted_token_issuer_arn: <p>Specifies the ARN of the trusted token issuer configuration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_trusted_token_issuer_request.DeleteTrustedTokenIssuerRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.delete_trusted_token_issuer_response.DeleteTrustedTokenIssuerResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_trusted_token_issuer

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_trusted_token_issuer.delete_trusted_token_issuer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_trusted_token_issuer_request.DeleteTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
        input_["trusted_token_issuer_arn"] = trusted_token_issuer_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_account_assignment_creation_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        account_assignment_creation_request_id: "aws_sdk_sso_admin.types.uu_id.UUId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_account_assignment_creation_status_response.DescribeAccountAssignmentCreationStatusResponse":
        r"""<p>Describes the status of the assignment creation request.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            account_assignment_creation_request_id: <p>The identifier that is used to track the request operation progress.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_account_assignment_creation_status_request.DescribeAccountAssignmentCreationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_account_assignment_creation_status_response.DescribeAccountAssignmentCreationStatusResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_account_assignment_creation_status

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_account_assignment_creation_status.describe_account_assignment_creation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_account_assignment_creation_status_request.DescribeAccountAssignmentCreationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["account_assignment_creation_request_id"] = (
            account_assignment_creation_request_id
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_account_assignment_deletion_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        account_assignment_deletion_request_id: "aws_sdk_sso_admin.types.uu_id.UUId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_account_assignment_deletion_status_response.DescribeAccountAssignmentDeletionStatusResponse":
        r"""<p>Describes the status of the assignment deletion request.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            account_assignment_deletion_request_id: <p>The identifier that is used to track the request operation progress.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_account_assignment_deletion_status_request.DescribeAccountAssignmentDeletionStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_account_assignment_deletion_status_response.DescribeAccountAssignmentDeletionStatusResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_account_assignment_deletion_status

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_account_assignment_deletion_status.describe_account_assignment_deletion_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_account_assignment_deletion_status_request.DescribeAccountAssignmentDeletionStatusRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["account_assignment_deletion_request_id"] = (
            account_assignment_deletion_request_id
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_application(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_application_response.DescribeApplicationResponse":
        r"""<p>Retrieves the details of an application associated with an instance of IAM Identity Center.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_application_request.DescribeApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_application_response.DescribeApplicationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_application

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_application.describe_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_application_request.DescribeApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_application_assignment(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_application_assignment_response.DescribeApplicationAssignmentResponse":
        r"""<p>Retrieves a direct assignment of a user or group to an application. If the user doesn’t have a direct assignment to the application, the user may still have access to the application through a group. Therefore, don’t use this API to test access to an application for a user. Instead use <a>ListApplicationAssignmentsForPrincipal</a>.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            principal_id: <p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html\">IAM Identity Center Identity Store API Reference</a>.</p>
            principal_type: <p>The entity type for which the assignment will be created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_application_assignment_request.DescribeApplicationAssignmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_application_assignment_response.DescribeApplicationAssignmentResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_application_assignment

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_application_assignment.describe_application_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_application_assignment_request.DescribeApplicationAssignmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["principal_id"] = principal_id
        input_["principal_type"] = principal_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_application_provider(
        self,
        application_provider_arn: "aws_sdk_sso_admin.types.application_provider_arn.ApplicationProviderArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_application_provider_response.DescribeApplicationProviderResponse":
        """<p>Retrieves details about a provider that can be used to connect an Amazon Web Services managed application or customer managed application to IAM Identity Center.</p>

        Args:
            application_provider_arn: <p>Specifies the ARN of the application provider for which you want details.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_application_provider_request.DescribeApplicationProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_application_provider_response.DescribeApplicationProviderResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_application_provider

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_application_provider.describe_application_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_application_provider_request.DescribeApplicationProviderRequest = {}  # type: ignore[typeddict-item]
        input_["application_provider_arn"] = application_provider_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_instance(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_instance_response.DescribeInstanceResponse":
        """<p>Returns the details of an instance of IAM Identity Center. The status can be one of the following:</p> <ul> <li> <p> <code>CREATE_IN_PROGRESS</code> - The instance is in the process of being created. When the instance is ready for use, DescribeInstance returns the status of <code>ACTIVE</code>. While the instance is in the <code>CREATE_IN_PROGRESS</code> state, you can call only DescribeInstance and DeleteInstance operations.</p> </li> <li> <p> <code>DELETE_IN_PROGRESS</code> - The instance is being deleted. Returns <code>AccessDeniedException</code> after the delete operation completes. </p> </li> <li> <p> <code>ACTIVE</code> - The instance is active.</p> </li> </ul>

        Args:
            instance_arn: <p>The ARN of the instance of IAM Identity Center under which the operation will run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_instance_request.DescribeInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_instance_response.DescribeInstanceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_instance

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_instance.describe_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_instance_request.DescribeInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_instance_access_control_attribute_configuration(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_instance_access_control_attribute_configuration_response.DescribeInstanceAccessControlAttributeConfigurationResponse":
        r"""<p>Returns the list of IAM Identity Center identity store attributes that have been configured to work with attributes-based access control (ABAC) for the specified IAM Identity Center instance. This will not return attributes configured and sent by an external identity provider. For more information about ABAC, see <a href=\"/singlesignon/latest/userguide/abac.html\">Attribute-Based Access Control</a> in the <i>IAM Identity Center User Guide</i>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_instance_access_control_attribute_configuration_request.DescribeInstanceAccessControlAttributeConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_instance_access_control_attribute_configuration_response.DescribeInstanceAccessControlAttributeConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_instance_access_control_attribute_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_instance_access_control_attribute_configuration.describe_instance_access_control_attribute_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_instance_access_control_attribute_configuration_request.DescribeInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_permission_set_response.DescribePermissionSetResponse":
        r"""<p>Gets the details of the permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_permission_set_request.DescribePermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_permission_set_response.DescribePermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_permission_set.describe_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_permission_set_request.DescribePermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_permission_set_provisioning_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        provision_permission_set_request_id: "aws_sdk_sso_admin.types.uu_id.UUId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_permission_set_provisioning_status_response.DescribePermissionSetProvisioningStatusResponse":
        r"""<p>Describes the status for the given permission set provisioning request.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            provision_permission_set_request_id: <p>The identifier that is provided by the <a>ProvisionPermissionSet</a> call to retrieve the current status of the provisioning workflow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_permission_set_provisioning_status_request.DescribePermissionSetProvisioningStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_permission_set_provisioning_status_response.DescribePermissionSetProvisioningStatusResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_permission_set_provisioning_status

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_permission_set_provisioning_status.describe_permission_set_provisioning_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_permission_set_provisioning_status_request.DescribePermissionSetProvisioningStatusRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["provision_permission_set_request_id"] = (
            provision_permission_set_request_id
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_region(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        region_name: "aws_sdk_sso_admin.types.region_name.RegionName",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_region_response.DescribeRegionResponse":
        r"""<p>Retrieves details about a specific Region enabled in an IAM Identity Center instance. Details include the Region name, current status (ACTIVE, ADDING, or REMOVING), the date when the Region was added, and whether it is the primary Region. The request must be made from one of the enabled Regions of the IAM Identity Center instance.</p> <p>The following actions are related to <code>DescribeRegion</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html\"> AddRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html\">RemoveRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html\">ListRegions</a> </p> </li> </ul>

        Args:
            instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance.</p>
            region_name: <p>The name of the Amazon Web Services Region to retrieve information about. The Region name must be 1-32 characters long and follow the pattern of Amazon Web Services Region names (for example, us-east-1).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_region_request.DescribeRegionRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_region_response.DescribeRegionResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_region

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_region.describe_region(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_region_request.DescribeRegionRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["region_name"] = region_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_trusted_token_issuer(
        self,
        trusted_token_issuer_arn: "aws_sdk_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.describe_trusted_token_issuer_response.DescribeTrustedTokenIssuerResponse":
        """<p>Retrieves details about a trusted token issuer configuration stored in an instance of IAM Identity Center. Details include the name of the trusted token issuer, the issuer URL, and the path of the source attribute and the destination attribute for a trusted token issuer configuration. </p>

        Args:
            trusted_token_issuer_arn: <p>Specifies the ARN of the trusted token issuer configuration that you want details about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.describe_trusted_token_issuer_request.DescribeTrustedTokenIssuerRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.describe_trusted_token_issuer_response.DescribeTrustedTokenIssuerResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.describe_trusted_token_issuer

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.describe_trusted_token_issuer.describe_trusted_token_issuer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.describe_trusted_token_issuer_request.DescribeTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
        input_["trusted_token_issuer_arn"] = trusted_token_issuer_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def detach_customer_managed_policy_reference_from_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        customer_managed_policy_reference: "aws_sdk_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.detach_customer_managed_policy_reference_from_permission_set_response.DetachCustomerManagedPolicyReferenceFromPermissionSetResponse":
        """<p>Detaches the specified customer managed policy from the specified <a>PermissionSet</a>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>
            permission_set_arn: <p>The ARN of the <code>PermissionSet</code>.</p>
            customer_managed_policy_reference: <p>Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each Amazon Web Services account where you want to deploy your permission set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.detach_customer_managed_policy_reference_from_permission_set_request.DetachCustomerManagedPolicyReferenceFromPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.detach_customer_managed_policy_reference_from_permission_set_response.DetachCustomerManagedPolicyReferenceFromPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.detach_customer_managed_policy_reference_from_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.detach_customer_managed_policy_reference_from_permission_set.detach_customer_managed_policy_reference_from_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.detach_customer_managed_policy_reference_from_permission_set_request.DetachCustomerManagedPolicyReferenceFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        input_["customer_managed_policy_reference"] = customer_managed_policy_reference

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def detach_managed_policy_from_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        managed_policy_arn: "aws_sdk_sso_admin.types.managed_policy_arn.ManagedPolicyArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.detach_managed_policy_from_permission_set_response.DetachManagedPolicyFromPermissionSetResponse":
        r"""<p>Detaches the attached Amazon Web Services managed policy ARN from the specified permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the <a>PermissionSet</a> from which the policy should be detached.</p>
            managed_policy_arn: <p>The Amazon Web Services managed policy ARN to be detached from a permission set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.detach_managed_policy_from_permission_set_request.DetachManagedPolicyFromPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.detach_managed_policy_from_permission_set_response.DetachManagedPolicyFromPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.detach_managed_policy_from_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.detach_managed_policy_from_permission_set.detach_managed_policy_from_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.detach_managed_policy_from_permission_set_request.DetachManagedPolicyFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        input_["managed_policy_arn"] = managed_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_application_assignment_configuration(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_application_assignment_configuration_response.GetApplicationAssignmentConfigurationResponse":
        r"""<p>Retrieves the configuration of <a>PutApplicationAssignmentConfiguration</a>.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.get_application_assignment_configuration_request.GetApplicationAssignmentConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.get_application_assignment_configuration_response.GetApplicationAssignmentConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_application_assignment_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.get_application_assignment_configuration.get_application_assignment_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.get_application_assignment_configuration_request.GetApplicationAssignmentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_application_session_configuration(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_application_session_configuration_response.GetApplicationSessionConfigurationResponse":
        """<p>Retrieves the session configuration for an application in IAM Identity Center.</p> <p>The session configuration determines how users can access an application. This includes whether user background sessions are enabled. User background sessions allow users to start a job on a supported Amazon Web Services managed application without having to remain signed in to an active session while the job runs.</p>

        Args:
            application_arn: <p>The Amazon Resource Name (ARN) of the application for which to retrieve the session configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.get_application_session_configuration_request.GetApplicationSessionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.get_application_session_configuration_response.GetApplicationSessionConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_application_session_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.get_application_session_configuration.get_application_session_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.get_application_session_configuration_request.GetApplicationSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_inline_policy_for_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_inline_policy_for_permission_set_response.GetInlinePolicyForPermissionSetResponse":
        r"""<p>Obtains the inline policy assigned to the permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.get_inline_policy_for_permission_set_request.GetInlinePolicyForPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.get_inline_policy_for_permission_set_response.GetInlinePolicyForPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_inline_policy_for_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.get_inline_policy_for_permission_set.get_inline_policy_for_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.get_inline_policy_for_permission_set_request.GetInlinePolicyForPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_permissions_boundary_for_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_permissions_boundary_for_permission_set_response.GetPermissionsBoundaryForPermissionSetResponse":
        """<p>Obtains the permissions boundary for a specified <a>PermissionSet</a>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>
            permission_set_arn: <p>The ARN of the <code>PermissionSet</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.get_permissions_boundary_for_permission_set_request.GetPermissionsBoundaryForPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.get_permissions_boundary_for_permission_set_response.GetPermissionsBoundaryForPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_permissions_boundary_for_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.get_permissions_boundary_for_permission_set.get_permissions_boundary_for_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.get_permissions_boundary_for_permission_set_request.GetPermissionsBoundaryForPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_account_assignment_creation_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.list_account_assignment_creation_status_response.ListAccountAssignmentCreationStatusResponse":
        r"""<p>Lists the status of the Amazon Web Services account assignment creation requests for a specified IAM Identity Center instance.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            max_results: <p>The maximum number of results to display for the assignment.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
            filter: <p>Filters results based on the passed attribute value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_account_assignment_creation_status_request.ListAccountAssignmentCreationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_account_assignment_creation_status_response.ListAccountAssignmentCreationStatusResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_account_assignment_creation_status

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_account_assignment_creation_status.list_account_assignment_creation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_account_assignment_creation_status_request.ListAccountAssignmentCreationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_account_assignment_creation_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
        ] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.account_assignment_operation_status_metadata.AccountAssignmentOperationStatusMetadata]":
        _token = next_token
        while True:
            _response = self.list_account_assignment_creation_status(
                instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("account_assignments_creation_status",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_account_assignment_deletion_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.list_account_assignment_deletion_status_response.ListAccountAssignmentDeletionStatusResponse":
        r"""<p>Lists the status of the Amazon Web Services account assignment deletion requests for a specified IAM Identity Center instance.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            max_results: <p>The maximum number of results to display for the assignment.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
            filter: <p>Filters results based on the passed attribute value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_account_assignment_deletion_status_request.ListAccountAssignmentDeletionStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_account_assignment_deletion_status_response.ListAccountAssignmentDeletionStatusResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_account_assignment_deletion_status

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_account_assignment_deletion_status.list_account_assignment_deletion_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_account_assignment_deletion_status_request.ListAccountAssignmentDeletionStatusRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_account_assignment_deletion_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
        ] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.account_assignment_operation_status_metadata.AccountAssignmentOperationStatusMetadata]":
        _token = next_token
        while True:
            _response = self.list_account_assignment_deletion_status(
                instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("account_assignments_deletion_status",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_account_assignments(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        account_id: "aws_sdk_sso_admin.types.target_id.TargetId",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_account_assignments_response.ListAccountAssignmentsResponse":
        r"""<p>Lists the assignee of the specified Amazon Web Services account with the specified permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            account_id: <p>The identifier of the Amazon Web Services account from which to list the assignments.</p>
            permission_set_arn: <p>The ARN of the permission set from which to list assignments.</p>
            max_results: <p>The maximum number of results to display for the assignment.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_account_assignments_request.ListAccountAssignmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_account_assignments_response.ListAccountAssignmentsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_account_assignments

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_account_assignments.list_account_assignments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_account_assignments_request.ListAccountAssignmentsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["account_id"] = account_id
        input_["permission_set_arn"] = permission_set_arn
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

    def iter_list_account_assignments(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        account_id: "aws_sdk_sso_admin.types.target_id.TargetId",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.account_assignment.AccountAssignment]":
        _token = next_token
        while True:
            _response = self.list_account_assignments(
                instance_arn,
                account_id,
                permission_set_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("account_assignments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_account_assignments_for_principal(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.list_account_assignments_filter.ListAccountAssignmentsFilter"
        ] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_sso_admin.types.list_account_assignments_for_principal_response.ListAccountAssignmentsForPrincipalResponse":
        """<p>Retrieves a list of the IAM Identity Center associated Amazon Web Services accounts that the principal has access to. This action must be called from the management account containing your organization instance of IAM Identity Center. This action is not valid for account instances of IAM Identity Center.</p>

        Args:
            instance_arn: <p>Specifies the ARN of the instance of IAM Identity Center that contains the principal.</p>
            principal_id: <p>Specifies the principal for which you want to retrieve the list of account assignments.</p>
            principal_type: <p>Specifies the type of the principal.</p>
            filter: <p>Specifies an Amazon Web Services account ID number. Results are filtered to only those that match this ID number.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_account_assignments_for_principal_request.ListAccountAssignmentsForPrincipalRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_account_assignments_for_principal_response.ListAccountAssignmentsForPrincipalResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_account_assignments_for_principal

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_account_assignments_for_principal.list_account_assignments_for_principal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_account_assignments_for_principal_request.ListAccountAssignmentsForPrincipalRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["principal_id"] = principal_id
        input_["principal_type"] = principal_type
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_account_assignments_for_principal(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.list_account_assignments_filter.ListAccountAssignmentsFilter"
        ] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.account_assignment_for_principal.AccountAssignmentForPrincipal]":
        _token = next_token
        while True:
            _response = self.list_account_assignments_for_principal(
                instance_arn,
                principal_id,
                principal_type,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("account_assignments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_accounts_for_provisioned_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        provisioning_status: Optional[
            "aws_sdk_sso_admin.types.provisioning_status.ProvisioningStatus"
        ] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_accounts_for_provisioned_permission_set_response.ListAccountsForProvisionedPermissionSetResponse":
        r"""<p>Lists all the Amazon Web Services accounts where the specified permission set is provisioned.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the <a>PermissionSet</a> from which the associated Amazon Web Services accounts will be listed.</p>
            provisioning_status: <p>The permission set provisioning status for an Amazon Web Services account.</p>
            max_results: <p>The maximum number of results to display for the <a>PermissionSet</a>.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_accounts_for_provisioned_permission_set_request.ListAccountsForProvisionedPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_accounts_for_provisioned_permission_set_response.ListAccountsForProvisionedPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_accounts_for_provisioned_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_accounts_for_provisioned_permission_set.list_accounts_for_provisioned_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_accounts_for_provisioned_permission_set_request.ListAccountsForProvisionedPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        if provisioning_status is not None:
            input_["provisioning_status"] = provisioning_status
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

    def iter_list_accounts_for_provisioned_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        provisioning_status: Optional[
            "aws_sdk_sso_admin.types.provisioning_status.ProvisioningStatus"
        ] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.account_id.AccountId]":
        _token = next_token
        while True:
            _response = self.list_accounts_for_provisioned_permission_set(
                instance_arn,
                permission_set_arn,
                config_overrides=config_overrides,
                provisioning_status=provisioning_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("account_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_application_assignments(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_assignments_response.ListApplicationAssignmentsResponse":
        """<p>Lists Amazon Web Services account users that are assigned to an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_application_assignments_request.ListApplicationAssignmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_application_assignments_response.ListApplicationAssignmentsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_assignments

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_application_assignments.list_application_assignments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_application_assignments_request.ListApplicationAssignmentsRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
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

    def iter_list_application_assignments(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> (
        "Iterator[aws_sdk_sso_admin.types.application_assignment.ApplicationAssignment]"
    ):
        _token = next_token
        while True:
            _response = self.list_application_assignments(
                application_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("application_assignments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_application_assignments_for_principal(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.list_application_assignments_filter.ListApplicationAssignmentsFilter"
        ] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_assignments_for_principal_response.ListApplicationAssignmentsForPrincipalResponse":
        """<p>Lists the applications to which a specified principal is assigned. You must provide a filter when calling this action from a member account against your organization instance of IAM Identity Center. A filter is not required when called from the management account against an organization instance of IAM Identity Center, or from a member account against an account instance of IAM Identity Center in the same account.</p>

        Args:
            instance_arn: <p>Specifies the instance of IAM Identity Center that contains principal and applications.</p>
            principal_id: <p>Specifies the unique identifier of the principal for which you want to retrieve its assignments.</p>
            principal_type: <p>Specifies the type of the principal for which you want to retrieve its assignments.</p>
            filter: <p>Filters the output to include only assignments associated with the application that has the specified ARN.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_application_assignments_for_principal_request.ListApplicationAssignmentsForPrincipalRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_application_assignments_for_principal_response.ListApplicationAssignmentsForPrincipalResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_assignments_for_principal

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_application_assignments_for_principal.list_application_assignments_for_principal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_application_assignments_for_principal_request.ListApplicationAssignmentsForPrincipalRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["principal_id"] = principal_id
        input_["principal_type"] = principal_type
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_application_assignments_for_principal(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId",
        principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.list_application_assignments_filter.ListApplicationAssignmentsFilter"
        ] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.application_assignment_for_principal.ApplicationAssignmentForPrincipal]":
        _token = next_token
        while True:
            _response = self.list_application_assignments_for_principal(
                instance_arn,
                principal_id,
                principal_type,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_assignments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_application_providers(
        self,
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_providers_response.ListApplicationProvidersResponse":
        """<p>Lists the application providers configured in the IAM Identity Center identity store.</p>

        Args:
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_application_providers_request.ListApplicationProvidersRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_application_providers_response.ListApplicationProvidersResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_providers

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_application_providers.list_application_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_application_providers_request.ListApplicationProvidersRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_application_providers(
        self,
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.application_provider.ApplicationProvider]":
        _token = next_token
        while True:
            _response = self.list_application_providers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("application_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_applications(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.list_applications_filter.ListApplicationsFilter"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.list_applications_response.ListApplicationsResponse":
        r"""<p>Lists all applications associated with the instance of IAM Identity Center. When listing applications for an organization instance in the management account, member accounts must use the <code>applicationAccount</code> parameter to filter the list to only applications created from that account. When listing applications for an account instance in the same member account, a filter is not required.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center application under which the operation will run. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            filter: <p>Filters response results. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_applications

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_applications(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.list_applications_filter.ListApplicationsFilter"
        ] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.application.Application]":
        _token = next_token
        while True:
            _response = self.list_applications(
                instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_customer_managed_policy_references_in_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_customer_managed_policy_references_in_permission_set_response.ListCustomerManagedPolicyReferencesInPermissionSetResponse":
        """<p>Lists all customer managed policies attached to a specified <a>PermissionSet</a>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>
            permission_set_arn: <p>The ARN of the <code>PermissionSet</code>. </p>
            max_results: <p>The maximum number of results to display for the list call.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_customer_managed_policy_references_in_permission_set_request.ListCustomerManagedPolicyReferencesInPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_customer_managed_policy_references_in_permission_set_response.ListCustomerManagedPolicyReferencesInPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_customer_managed_policy_references_in_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_customer_managed_policy_references_in_permission_set.list_customer_managed_policy_references_in_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_customer_managed_policy_references_in_permission_set_request.ListCustomerManagedPolicyReferencesInPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
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

    def iter_list_customer_managed_policy_references_in_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference]":
        _token = next_token
        while True:
            _response = self.list_customer_managed_policy_references_in_permission_set(
                instance_arn,
                permission_set_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("customer_managed_policy_references",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_instances(
        self,
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_instances_response.ListInstancesResponse":
        """<p>Lists the details of the organization and account instances of IAM Identity Center that were created in or visible to the account calling this API. </p>

        Args:
            max_results: <p>The maximum number of results to display for the instance.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_instances_request.ListInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_instances_response.ListInstancesResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_instances

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_instances.list_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_instances_request.ListInstancesRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_instances(
        self,
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.instance_metadata.InstanceMetadata]":
        _token = next_token
        while True:
            _response = self.list_instances(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_managed_policies_in_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_managed_policies_in_permission_set_response.ListManagedPoliciesInPermissionSetResponse":
        r"""<p>Lists the Amazon Web Services managed policy that is attached to a specified permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the <a>PermissionSet</a> whose managed policies will be listed.</p>
            max_results: <p>The maximum number of results to display for the <a>PermissionSet</a>.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_managed_policies_in_permission_set_request.ListManagedPoliciesInPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_managed_policies_in_permission_set_response.ListManagedPoliciesInPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_managed_policies_in_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_managed_policies_in_permission_set.list_managed_policies_in_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_managed_policies_in_permission_set_request.ListManagedPoliciesInPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
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

    def iter_list_managed_policies_in_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.attached_managed_policy.AttachedManagedPolicy]":
        _token = next_token
        while True:
            _response = self.list_managed_policies_in_permission_set(
                instance_arn,
                permission_set_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("attached_managed_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_set_provisioning_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.list_permission_set_provisioning_status_response.ListPermissionSetProvisioningStatusResponse":
        r"""<p>Lists the status of the permission set provisioning requests for a specified IAM Identity Center instance.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            max_results: <p>The maximum number of results to display for the assignment.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
            filter: <p>Filters results based on the passed attribute value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_permission_set_provisioning_status_request.ListPermissionSetProvisioningStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_permission_set_provisioning_status_response.ListPermissionSetProvisioningStatusResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_permission_set_provisioning_status

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_permission_set_provisioning_status.list_permission_set_provisioning_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_permission_set_provisioning_status_request.ListPermissionSetProvisioningStatusRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_permission_set_provisioning_status(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        filter: Optional[
            "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
        ] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata.PermissionSetProvisioningStatusMetadata]":
        _token = next_token
        while True:
            _response = self.list_permission_set_provisioning_status(
                instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("permission_sets_provisioning_status",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_sets(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_sso_admin.types.list_permission_sets_response.ListPermissionSetsResponse":
        r"""<p>Lists the <a>PermissionSet</a>s in an IAM Identity Center instance.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
            max_results: <p>The maximum number of results to display for the assignment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_permission_sets_request.ListPermissionSetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_permission_sets_response.ListPermissionSetsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_permission_sets

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_permission_sets.list_permission_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_permission_sets_request.ListPermissionSetsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_permission_sets(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn]":
        _token = next_token
        while True:
            _response = self.list_permission_sets(
                instance_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("permission_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permission_sets_provisioned_to_account(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        account_id: "aws_sdk_sso_admin.types.account_id.AccountId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        provisioning_status: Optional[
            "aws_sdk_sso_admin.types.provisioning_status.ProvisioningStatus"
        ] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_permission_sets_provisioned_to_account_response.ListPermissionSetsProvisionedToAccountResponse":
        r"""<p>Lists all the permission sets that are provisioned to a specified Amazon Web Services account.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            account_id: <p>The identifier of the Amazon Web Services account from which to list the assignments.</p>
            provisioning_status: <p>The status object for the permission set provisioning operation.</p>
            max_results: <p>The maximum number of results to display for the assignment.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_permission_sets_provisioned_to_account_request.ListPermissionSetsProvisionedToAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_permission_sets_provisioned_to_account_response.ListPermissionSetsProvisionedToAccountResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_permission_sets_provisioned_to_account

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_permission_sets_provisioned_to_account.list_permission_sets_provisioned_to_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_permission_sets_provisioned_to_account_request.ListPermissionSetsProvisionedToAccountRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["account_id"] = account_id
        if provisioning_status is not None:
            input_["provisioning_status"] = provisioning_status
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

    def iter_list_permission_sets_provisioned_to_account(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        account_id: "aws_sdk_sso_admin.types.account_id.AccountId",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        provisioning_status: Optional[
            "aws_sdk_sso_admin.types.provisioning_status.ProvisioningStatus"
        ] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn]":
        _token = next_token
        while True:
            _response = self.list_permission_sets_provisioned_to_account(
                instance_arn,
                account_id,
                config_overrides=config_overrides,
                provisioning_status=provisioning_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permission_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_regions(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_regions_response.ListRegionsResponse":
        r"""<p>Lists all enabled Regions of an IAM Identity Center instance, including those that are being added or removed. This operation returns Regions with ACTIVE, ADDING, or REMOVING status.</p> <p>The following actions are related to <code>ListRegions</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html\"> AddRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html\">RemoveRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html\">DescribeRegion</a> </p> </li> </ul>

        Args:
            instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance.</p>
            max_results: <p>The maximum number of results to return in a single call. Default is 100.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_regions_request.ListRegionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_regions_response.ListRegionsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_regions

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_regions.list_regions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_regions_request.ListRegionsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
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

    def iter_list_regions(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.region_metadata.RegionMetadata]":
        _token = next_token
        while True:
            _response = self.list_regions(
                instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("regions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_sso_admin.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        instance_arn: Optional[
            "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
        ] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Lists the tags that are attached to a specified resource.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            resource_arn: <p>The ARN of the resource with the tags to be listed.</p>
            next_token: <p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        if instance_arn is not None:
            input_["instance_arn"] = instance_arn
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_sso_admin.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        instance_arn: Optional[
            "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
        ] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.tag.Tag]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                instance_arn=instance_arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_trusted_token_issuers(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_trusted_token_issuers_response.ListTrustedTokenIssuersResponse":
        """<p>Lists all the trusted token issuers configured in an instance of IAM Identity Center.</p>

        Args:
            instance_arn: <p>Specifies the ARN of the instance of IAM Identity Center with the trusted token issuer configurations that you want to list.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_trusted_token_issuers_request.ListTrustedTokenIssuersRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_trusted_token_issuers_response.ListTrustedTokenIssuersResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_trusted_token_issuers

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_trusted_token_issuers.list_trusted_token_issuers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_trusted_token_issuers_request.ListTrustedTokenIssuersRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
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

    def iter_list_trusted_token_issuers(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["aws_sdk_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "Iterator[aws_sdk_sso_admin.types.trusted_token_issuer_metadata.TrustedTokenIssuerMetadata]":
        _token = next_token
        while True:
            _response = self.list_trusted_token_issuers(
                instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("trusted_token_issuers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def provision_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        target_type: "aws_sdk_sso_admin.types.provision_target_type.ProvisionTargetType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        target_id: Optional["aws_sdk_sso_admin.types.target_id.TargetId"] = None,
    ) -> "aws_sdk_sso_admin.types.provision_permission_set_response.ProvisionPermissionSetResponse":
        r"""<p>The process by which a specified permission set is provisioned to the specified target.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set.</p>
            target_id: <p>TargetID is an Amazon Web Services account identifier, (For example, 123456789012).</p>
            target_type: <p>The entity type for which the assignment will be created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.provision_permission_set_request.ProvisionPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.provision_permission_set_response.ProvisionPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.provision_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.provision_permission_set.provision_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.provision_permission_set_request.ProvisionPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        if target_id is not None:
            input_["target_id"] = target_id
        input_["target_type"] = target_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_application_assignment_configuration(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        assignment_required: "aws_sdk_sso_admin.types.assignment_required.AssignmentRequired",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.put_application_assignment_configuration_response.PutApplicationAssignmentConfigurationResponse":
        r"""<p>Configure how users gain access to an application. If <code>AssignmentsRequired</code> is <code>true</code> (default value), users don’t have access to the application unless an assignment is created using the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html\">CreateApplicationAssignment API</a>. If <code>false</code>, all users have access to the application. If an assignment is created using <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html\">CreateApplicationAssignment</a>., the user retains access if <code>AssignmentsRequired</code> is set to <code>true</code>. </p>

        Args:
            application_arn: <p>Specifies the ARN of the application. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            assignment_required: <p>If <code>AssignmentsRequired</code> is <code>true</code> (default value), users don’t have access to the application unless an assignment is created using the <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html\">CreateApplicationAssignment API</a>. If <code>false</code>, all users have access to the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.put_application_assignment_configuration_request.PutApplicationAssignmentConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.put_application_assignment_configuration_response.PutApplicationAssignmentConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_application_assignment_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.put_application_assignment_configuration.put_application_assignment_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.put_application_assignment_configuration_request.PutApplicationAssignmentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["assignment_required"] = assignment_required

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_application_session_configuration(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        user_background_session_application_status: Optional[
            "aws_sdk_sso_admin.types.user_background_session_application_status.UserBackgroundSessionApplicationStatus"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.put_application_session_configuration_response.PutApplicationSessionConfigurationResponse":
        """<p>Updates the session configuration for an application in IAM Identity Center.</p> <p>The session configuration determines how users can access an application. This includes whether user background sessions are enabled. User background sessions allow users to start a job on a supported Amazon Web Services managed application without having to remain signed in to an active session while the job runs.</p>

        Args:
            application_arn: <p>The Amazon Resource Name (ARN) of the application for which to update the session configuration.</p>
            user_background_session_application_status: <p>The status of user background sessions for the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.put_application_session_configuration_request.PutApplicationSessionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.put_application_session_configuration_response.PutApplicationSessionConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_application_session_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.put_application_session_configuration.put_application_session_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.put_application_session_configuration_request.PutApplicationSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        if user_background_session_application_status is not None:
            input_["user_background_session_application_status"] = (
                user_background_session_application_status
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_inline_policy_to_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        inline_policy: "aws_sdk_sso_admin.types.permission_set_policy_document.PermissionSetPolicyDocument",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.put_inline_policy_to_permission_set_response.PutInlinePolicyToPermissionSetResponse":
        r"""<p>Attaches an inline policy to a permission set.</p> <note> <p>If the permission set is already referenced by one or more account assignments, you will need to call <code> <a>ProvisionPermissionSet</a> </code> after this action to apply the corresponding IAM policy updates to all assigned accounts.</p> </note>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set.</p>
            inline_policy: <p>The inline policy to attach to a <a>PermissionSet</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.put_inline_policy_to_permission_set_request.PutInlinePolicyToPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.put_inline_policy_to_permission_set_response.PutInlinePolicyToPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_inline_policy_to_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.put_inline_policy_to_permission_set.put_inline_policy_to_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.put_inline_policy_to_permission_set_request.PutInlinePolicyToPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        input_["inline_policy"] = inline_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_permissions_boundary_to_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        permissions_boundary: "aws_sdk_sso_admin.types.permissions_boundary.PermissionsBoundary",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.put_permissions_boundary_to_permission_set_response.PutPermissionsBoundaryToPermissionSetResponse":
        """<p>Attaches an Amazon Web Services managed or customer managed policy to the specified <a>PermissionSet</a> as a permissions boundary.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>
            permission_set_arn: <p>The ARN of the <code>PermissionSet</code>.</p>
            permissions_boundary: <p>The permissions boundary that you want to attach to a <code>PermissionSet</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.put_permissions_boundary_to_permission_set_request.PutPermissionsBoundaryToPermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.put_permissions_boundary_to_permission_set_response.PutPermissionsBoundaryToPermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_permissions_boundary_to_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.put_permissions_boundary_to_permission_set.put_permissions_boundary_to_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.put_permissions_boundary_to_permission_set_request.PutPermissionsBoundaryToPermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        input_["permissions_boundary"] = permissions_boundary

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_region(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        region_name: "aws_sdk_sso_admin.types.region_name.RegionName",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.remove_region_response.RemoveRegionResponse":
        r"""<p>Removes an additional Region from an IAM Identity Center instance. This operation initiates an asynchronous workflow to clean up IAM Identity Center resources in the specified additional Region. The Region status is set to REMOVING and the Region record is deleted when the workflow completes. The request must be made from the primary Region. The target Region cannot be the primary Region, and no other add or remove Region workflows can be in progress.</p> <p>The following actions are related to <code>RemoveRegion</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html\"> AddRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html\">DescribeRegion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html\">ListRegions</a> </p> </li> </ul>

        Args:
            instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance.</p>
            region_name: <p>The name of the Amazon Web Services Region to remove from the IAM Identity Center instance. The Region name must be 1-32 characters long and follow the pattern of Amazon Web Services Region names (for example, us-east-1). The primary Region cannot be removed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.remove_region_request.RemoveRegionRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.remove_region_response.RemoveRegionResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.remove_region

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.remove_region.remove_region(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.remove_region_request.RemoveRegionRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["region_name"] = region_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_sso_admin.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_sso_admin.types.tag_list.TagList",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        instance_arn: Optional[
            "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.tag_resource_response.TagResourceResponse":
        r"""<p>Associates a set of tags with a specified resource.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            resource_arn: <p>The ARN of the resource with the tags to be listed.</p>
            tags: <p>A set of key-value pairs that are used to manage the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.tag_resource

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        if instance_arn is not None:
            input_["instance_arn"] = instance_arn
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
        resource_arn: "aws_sdk_sso_admin.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_sso_admin.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        instance_arn: Optional[
            "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Disassociates a set of tags from a specified resource.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            resource_arn: <p>The ARN of the resource with the tags to be listed.</p>
            tag_keys: <p>The keys of tags that are attached to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.untag_resource

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        if instance_arn is not None:
            input_["instance_arn"] = instance_arn
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_application(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        name: Optional[
            "aws_sdk_sso_admin.types.application_name_type.ApplicationNameType"
        ] = None,
        description: Optional["aws_sdk_sso_admin.types.description.Description"] = None,
        status: Optional[
            "aws_sdk_sso_admin.types.application_status.ApplicationStatus"
        ] = None,
        portal_options: Optional[
            "aws_sdk_sso_admin.types.update_application_portal_options.UpdateApplicationPortalOptions"
        ] = None,
    ) -> (
        "aws_sdk_sso_admin.types.update_application_response.UpdateApplicationResponse"
    ):
        r"""<p>Updates application properties. </p>

        Args:
            application_arn: <p>Specifies the ARN of the application. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            name: <p>Specifies the updated name for the application.</p>
            description: <p>The description of the .</p>
            status: <p>Specifies whether the application is enabled or disabled.</p>
            portal_options: <p>A structure that describes the options for the portal associated with an application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.update_application_response.UpdateApplicationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.update_application

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if portal_options is not None:
            input_["portal_options"] = portal_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_instance(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        name: Optional["aws_sdk_sso_admin.types.name_type.NameType"] = None,
        encryption_configuration: Optional[
            "aws_sdk_sso_admin.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.update_instance_response.UpdateInstanceResponse":
        r"""<p>Update the details for the instance of IAM Identity Center that is owned by the Amazon Web Services account.</p>

        Args:
            name: <p>Updates the instance name.</p>
            instance_arn: <p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            encryption_configuration: <p>Specifies the encryption configuration for your IAM Identity Center instance. You can use this to configure customer managed KMS keys or Amazon Web Services owned KMS keys for encrypting your instance data.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.update_instance_request.UpdateInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.update_instance_response.UpdateInstanceResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.update_instance

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.update_instance.update_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.update_instance_request.UpdateInstanceRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        input_["instance_arn"] = instance_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_instance_access_control_attribute_configuration(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        instance_access_control_attribute_configuration: "aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.InstanceAccessControlAttributeConfiguration",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.update_instance_access_control_attribute_configuration_response.UpdateInstanceAccessControlAttributeConfigurationResponse":
        r"""<p>Updates the IAM Identity Center identity store attributes that you can use with the IAM Identity Center instance for attributes-based access control (ABAC). When using an external identity provider as an identity source, you can pass attributes through the SAML assertion as an alternative to configuring attributes from the IAM Identity Center identity store. If a SAML assertion passes any of these attributes, IAM Identity Center replaces the attribute value with the value from the IAM Identity Center identity store. For more information about ABAC, see <a href=\"/singlesignon/latest/userguide/abac.html\">Attribute-Based Access Control</a> in the <i>IAM Identity Center User Guide</i>.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>
            instance_access_control_attribute_configuration: <p>Updates the attributes for your ABAC configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.update_instance_access_control_attribute_configuration_request.UpdateInstanceAccessControlAttributeConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.update_instance_access_control_attribute_configuration_response.UpdateInstanceAccessControlAttributeConfigurationResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.update_instance_access_control_attribute_configuration

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.update_instance_access_control_attribute_configuration.update_instance_access_control_attribute_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.update_instance_access_control_attribute_configuration_request.UpdateInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["instance_access_control_attribute_configuration"] = (
            instance_access_control_attribute_configuration
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_permission_set(
        self,
        instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn",
        permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        description: Optional[
            "aws_sdk_sso_admin.types.permission_set_description.PermissionSetDescription"
        ] = None,
        session_duration: Optional["aws_sdk_sso_admin.types.duration.Duration"] = None,
        relay_state: Optional["aws_sdk_sso_admin.types.relay_state.RelayState"] = None,
    ) -> "aws_sdk_sso_admin.types.update_permission_set_response.UpdatePermissionSetResponse":
        r"""<p>Updates an existing permission set.</p>

        Args:
            instance_arn: <p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            permission_set_arn: <p>The ARN of the permission set.</p>
            description: <p>The description of the <a>PermissionSet</a>.</p>
            session_duration: <p>The length of time that the application user sessions are valid for in the ISO-8601 standard.</p>
            relay_state: <p>Used to redirect users within the application during the federation authentication process.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.update_permission_set_request.UpdatePermissionSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.update_permission_set_response.UpdatePermissionSetResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.update_permission_set

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.update_permission_set.update_permission_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.update_permission_set_request.UpdatePermissionSetRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        input_["permission_set_arn"] = permission_set_arn
        if description is not None:
            input_["description"] = description
        if session_duration is not None:
            input_["session_duration"] = session_duration
        if relay_state is not None:
            input_["relay_state"] = relay_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_trusted_token_issuer(
        self,
        trusted_token_issuer_arn: "aws_sdk_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        name: Optional[
            "aws_sdk_sso_admin.types.trusted_token_issuer_name.TrustedTokenIssuerName"
        ] = None,
        trusted_token_issuer_configuration: Optional[
            "aws_sdk_sso_admin.types.trusted_token_issuer_update_configuration.TrustedTokenIssuerUpdateConfiguration"
        ] = None,
    ) -> "aws_sdk_sso_admin.types.update_trusted_token_issuer_response.UpdateTrustedTokenIssuerResponse":
        """<p>Updates the name of the trusted token issuer, or the path of a source attribute or destination attribute for a trusted token issuer configuration.</p> <note> <p>Updating this trusted token issuer configuration might cause users to lose access to any applications that are configured to use the trusted token issuer.</p> </note>

        Args:
            trusted_token_issuer_arn: <p>Specifies the ARN of the trusted token issuer configuration that you want to update.</p>
            name: <p>Specifies the updated name to be applied to the trusted token issuer configuration.</p>
            trusted_token_issuer_configuration: <p>Specifies a structure with settings to apply to the specified trusted token issuer. The settings that you can provide are determined by the type of the trusted token issuer that you are updating.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.update_trusted_token_issuer_request.UpdateTrustedTokenIssuerRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.update_trusted_token_issuer_response.UpdateTrustedTokenIssuerResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.update_trusted_token_issuer

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.update_trusted_token_issuer.update_trusted_token_issuer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.update_trusted_token_issuer_request.UpdateTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
        input_["trusted_token_issuer_arn"] = trusted_token_issuer_arn
        if name is not None:
            input_["name"] = name
        if trusted_token_issuer_configuration is not None:
            input_["trusted_token_issuer_configuration"] = (
                trusted_token_issuer_configuration
            )

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
