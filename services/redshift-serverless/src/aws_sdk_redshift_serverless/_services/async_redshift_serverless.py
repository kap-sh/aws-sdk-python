"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RedshiftServerless``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_redshift_serverless._auth._signers
import aws_sdk_redshift_serverless._auth._sigv4
from aws_sdk_redshift_serverless._auth._identity import Credentials
from aws_sdk_redshift_serverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_redshift_serverless._auth._zapros_handler import AuthMiddleware
from aws_sdk_redshift_serverless._pagination import resolve_path as _resolve_path
from aws_sdk_redshift_serverless._resources.redshift_serverless.cross_vpc_endpoint_resource import (
    AsyncCrossVpcEndpointResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.managed_workgroup_resource import (
    AsyncManagedWorkgroupResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.namespace_resource import (
    AsyncNamespaceResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.recovery_point_resource import (
    AsyncRecoveryPointResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.reservation_resource import (
    AsyncReservationResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.scheduled_action_resource import (
    AsyncScheduledActionResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.snapshot_resource import (
    AsyncSnapshotResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.usage_limit_resource import (
    AsyncUsageLimitResource,
)
from aws_sdk_redshift_serverless._resources.redshift_serverless.workgroup_resource import (
    AsyncWorkgroupResource,
)
from aws_sdk_redshift_serverless._services._aws_config import aaws_config
from aws_sdk_redshift_serverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.amazon_resource_name
    import aws_sdk_redshift_serverless.types.association
    import aws_sdk_redshift_serverless.types.create_custom_domain_association_request
    import aws_sdk_redshift_serverless.types.create_custom_domain_association_response
    import aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string
    import aws_sdk_redshift_serverless.types.custom_domain_name
    import aws_sdk_redshift_serverless.types.db_name
    import aws_sdk_redshift_serverless.types.delete_custom_domain_association_request
    import aws_sdk_redshift_serverless.types.delete_custom_domain_association_response
    import aws_sdk_redshift_serverless.types.delete_resource_policy_request
    import aws_sdk_redshift_serverless.types.delete_resource_policy_response
    import aws_sdk_redshift_serverless.types.get_credentials_request
    import aws_sdk_redshift_serverless.types.get_credentials_response
    import aws_sdk_redshift_serverless.types.get_custom_domain_association_request
    import aws_sdk_redshift_serverless.types.get_custom_domain_association_response
    import aws_sdk_redshift_serverless.types.get_identity_center_auth_token_request
    import aws_sdk_redshift_serverless.types.get_identity_center_auth_token_response
    import aws_sdk_redshift_serverless.types.get_resource_policy_request
    import aws_sdk_redshift_serverless.types.get_resource_policy_response
    import aws_sdk_redshift_serverless.types.get_track_request
    import aws_sdk_redshift_serverless.types.get_track_response
    import aws_sdk_redshift_serverless.types.list_custom_domain_associations_request
    import aws_sdk_redshift_serverless.types.list_custom_domain_associations_response
    import aws_sdk_redshift_serverless.types.list_tags_for_resource_request
    import aws_sdk_redshift_serverless.types.list_tags_for_resource_response
    import aws_sdk_redshift_serverless.types.list_tracks_request
    import aws_sdk_redshift_serverless.types.list_tracks_response
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.put_resource_policy_request
    import aws_sdk_redshift_serverless.types.put_resource_policy_response
    import aws_sdk_redshift_serverless.types.serverless_track
    import aws_sdk_redshift_serverless.types.tag_key_list
    import aws_sdk_redshift_serverless.types.tag_list
    import aws_sdk_redshift_serverless.types.tag_resource_request
    import aws_sdk_redshift_serverless.types.tag_resource_response
    import aws_sdk_redshift_serverless.types.track_name
    import aws_sdk_redshift_serverless.types.untag_resource_request
    import aws_sdk_redshift_serverless.types.untag_resource_response
    import aws_sdk_redshift_serverless.types.update_custom_domain_association_request
    import aws_sdk_redshift_serverless.types.update_custom_domain_association_response
    import aws_sdk_redshift_serverless.types.workgroup_name
    import aws_sdk_redshift_serverless.types.workgroup_name_list


class AsyncRedshiftServerlessClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncRedshiftServerlessClient:
    """A client for the ``RedshiftServerless`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncRedshiftServerlessClientConfig(
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

        # resources
        self.cross_vpc_endpoint_resource = AsyncCrossVpcEndpointResource(self)
        self.managed_workgroup_resource = AsyncManagedWorkgroupResource(self)
        self.namespace_resource = AsyncNamespaceResource(self)
        self.recovery_point_resource = AsyncRecoveryPointResource(self)
        self.reservation_resource = AsyncReservationResource(self)
        self.scheduled_action_resource = AsyncScheduledActionResource(self)
        self.snapshot_resource = AsyncSnapshotResource(self)
        self.usage_limit_resource = AsyncUsageLimitResource(self)
        self.workgroup_resource = AsyncWorkgroupResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRedshiftServerlessClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def create_custom_domain_association(
        self,
        workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName",
        custom_domain_name: "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName",
        custom_domain_certificate_arn: "aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_custom_domain_association_response.CreateCustomDomainAssociationResponse":
        """<p>Creates a custom domain association for Amazon Redshift Serverless.</p>

        Args:
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name to associate with the workgroup.</p>
            custom_domain_certificate_arn: <p>The custom domain name’s certificate Amazon resource name (ARN).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.create_custom_domain_association_request.CreateCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.create_custom_domain_association_response.CreateCustomDomainAssociationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_custom_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.create_custom_domain_association.async_create_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_custom_domain_association_request.CreateCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["workgroup_name"] = workgroup_name
        input_["custom_domain_name"] = custom_domain_name
        input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_custom_domain_association(
        self,
        workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName",
        custom_domain_name: "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_custom_domain_association_response.DeleteCustomDomainAssociationResponse":
        """<p>Deletes a custom domain association for Amazon Redshift Serverless.</p>

        Args:
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_custom_domain_association_request.DeleteCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_custom_domain_association_response.DeleteCustomDomainAssociationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_custom_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_custom_domain_association.async_delete_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_custom_domain_association_request.DeleteCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["workgroup_name"] = workgroup_name
        input_["custom_domain_name"] = custom_domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the specified resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the policy to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_credentials(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        db_name: Optional["aws_sdk_redshift_serverless.types.db_name.DbName"] = None,
        duration_seconds: Optional[int] = None,
        workgroup_name: Optional[
            "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
        ] = None,
        custom_domain_name: Optional[
            "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_credentials_response.GetCredentialsResponse":
        r"""<p>Returns a database user name and temporary password with temporary authorization to log in to Amazon Redshift Serverless.</p> <p>By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes).</p> <p>The Identity and Access Management (IAM) user or role that runs GetCredentials must have an IAM policy attached that allows access to all necessary actions and resources.</p> <p>If the <code>DbName</code> parameter is specified, the IAM policy must allow access to the resource dbname for the specified database name.</p>

        Args:
            db_name: <p>The name of the database to get temporary authorization to log on to.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens.</p> </li> <li> <p>Must contain only uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ).</p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href=\"https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\">Reserved Words </a> in the Amazon Redshift Database Developer Guide</p> </li> </ul>
            duration_seconds: <p>The number of seconds until the returned temporary password expires. The minimum is 900 seconds, and the maximum is 3600 seconds.</p>
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup. The custom domain name or the workgroup name must be included in the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_credentials_request.GetCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_credentials_response.GetCredentialsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_credentials

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_credentials.async_get_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_credentials_request.GetCredentialsRequest = {}  # type: ignore[typeddict-item]
        if db_name is not None:
            input_["db_name"] = db_name
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_custom_domain_association(
        self,
        custom_domain_name: "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName",
        workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_custom_domain_association_response.GetCustomDomainAssociationResponse":
        """<p>Gets information about a specific custom domain association.</p>

        Args:
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_custom_domain_association_request.GetCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_custom_domain_association_response.GetCustomDomainAssociationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_custom_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_custom_domain_association.async_get_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_custom_domain_association_request.GetCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["custom_domain_name"] = custom_domain_name
        input_["workgroup_name"] = workgroup_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_identity_center_auth_token(
        self,
        workgroup_names: "aws_sdk_redshift_serverless.types.workgroup_name_list.WorkgroupNameList",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_identity_center_auth_token_response.GetIdentityCenterAuthTokenResponse":
        """<p>Returns an Identity Center authentication token for accessing Amazon Redshift Serverless workgroups.</p> <p>The token provides secure access to data within the specified workgroups using Identity Center identity propagation. The token expires after a specified duration and must be refreshed for continued access.</p> <p>The Identity and Access Management (IAM) user or role that runs GetIdentityCenterAuthToken must have appropriate permissions to access the specified workgroups and Identity Center integration must be configured for the workgroups.</p>

        Args:
            workgroup_names: <p>A list of workgroup names for which to generate the Identity Center authentication token.</p> <p>Constraints:</p> <ul> <li> <p>Must contain between 1 and 20 workgroup names.</p> </li> <li> <p>Each workgroup name must be a valid Amazon Redshift Serverless workgroup identifier.</p> </li> <li> <p>All specified workgroups must have Identity Center integration enabled.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_identity_center_auth_token_request.GetIdentityCenterAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_identity_center_auth_token_response.GetIdentityCenterAuthTokenResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_identity_center_auth_token

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_identity_center_auth_token.async_get_identity_center_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_identity_center_auth_token_request.GetIdentityCenterAuthTokenRequest = {}  # type: ignore[typeddict-item]
        input_["workgroup_names"] = workgroup_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns a resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_track(
        self,
        track_name: "aws_sdk_redshift_serverless.types.track_name.TrackName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_track_response.GetTrackResponse":
        """<p>Get the Redshift Serverless version for a specified track.</p>

        Args:
            track_name: <p>The name of the track of which its version is fetched.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_track_request.GetTrackRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_track_response.GetTrackResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_track

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_track.async_get_track(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_track_request.GetTrackRequest = {}  # type: ignore[typeddict-item]
        input_["track_name"] = track_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_custom_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        custom_domain_name: Optional[
            "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_custom_domain_associations_response.ListCustomDomainAssociationsResponse":
        """<p> Lists custom domain associations for Amazon Redshift Serverless.</p>

        Args:
            next_token: <p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
            custom_domain_certificate_arn: <p>The custom domain name’s certificate Amazon resource name (ARN).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_custom_domain_associations_request.ListCustomDomainAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_custom_domain_associations_response.ListCustomDomainAssociationsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_custom_domain_associations

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_custom_domain_associations.async_list_custom_domain_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_custom_domain_associations_request.ListCustomDomainAssociationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if custom_domain_certificate_arn is not None:
            input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_custom_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        custom_domain_name: Optional[
            "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_redshift_serverless.types.association.Association]":
        _token = next_token
        while True:
            _response = await self.list_custom_domain_associations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                custom_domain_name=custom_domain_name,
                custom_domain_certificate_arn=custom_domain_certificate_arn,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_redshift_serverless.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tracks(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_tracks_response.ListTracksResponse":
        """<p>List the Amazon Redshift Serverless versions.</p>

        Args:
            next_token: <p>If your initial <code>ListTracksRequest</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListTracksRequest</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_tracks_request.ListTracksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_tracks_response.ListTracksResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_tracks

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_tracks.async_list_tracks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_tracks_request.ListTracksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_tracks(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[aws_sdk_redshift_serverless.types.serverless_track.ServerlessTrack]":
        _token = next_token
        while True:
            _response = await self.list_tracks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tracks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_resource_policy(
        self,
        resource_arn: str,
        policy: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.put_resource_policy_response.PutResourcePolicyResponse":
        r"""<p>Creates or updates a resource policy. Currently, you can use policies to share snapshots across Amazon Web Services accounts.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the account to create or update a resource policy for.</p>
            policy: <p>The policy to create or update. For example, the following policy grants a user authorization to restore a snapshot.</p> <p> <code>\"{\\"Version\\": \\"2012-10-17\\", \\"Statement\\" : [{ \\"Sid\\": \\"AllowUserRestoreFromSnapshot\\", \\"Principal\\":{\\"AWS\\": [\\"739247239426\\"]}, \\"Action\\": [\\"redshift-serverless:RestoreFromSnapshot\\"] , \\"Effect\\": \\"Allow\\" }]}\"</code> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_redshift_serverless.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_redshift_serverless.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The map of the key-value pairs used to tag the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_redshift_serverless.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_redshift_serverless.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or set of tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The tag or set of tags to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_custom_domain_association(
        self,
        workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName",
        custom_domain_name: "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName",
        custom_domain_certificate_arn: "aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_custom_domain_association_response.UpdateCustomDomainAssociationResponse":
        """<p>Updates an Amazon Redshift Serverless certificate associated with a custom domain.</p>

        Args:
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
            custom_domain_certificate_arn: <p>The custom domain name’s certificate Amazon resource name (ARN). This is optional.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_custom_domain_association_request.UpdateCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_custom_domain_association_response.UpdateCustomDomainAssociationResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_custom_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_custom_domain_association.async_update_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_custom_domain_association_request.UpdateCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["workgroup_name"] = workgroup_name
        input_["custom_domain_name"] = custom_domain_name
        input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
