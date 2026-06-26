"""Generated from Smithy shape ``com.amazonaws.signer#WallabyService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_signer._auth._signers
import aws_sdk_signer._auth._sigv4
from aws_sdk_signer._auth._identity import Credentials
from aws_sdk_signer._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_signer._auth._zapros_handler import AuthMiddleware
from aws_sdk_signer._services._aws_config import aws_config
from aws_sdk_signer._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_signer.types.account_id
    import aws_sdk_signer.types.add_profile_permission_request
    import aws_sdk_signer.types.add_profile_permission_response
    import aws_sdk_signer.types.arn
    import aws_sdk_signer.types.bool
    import aws_sdk_signer.types.cancel_signing_profile_request
    import aws_sdk_signer.types.certificate_hashes
    import aws_sdk_signer.types.client_request_token
    import aws_sdk_signer.types.describe_signing_job_request
    import aws_sdk_signer.types.describe_signing_job_response
    import aws_sdk_signer.types.destination
    import aws_sdk_signer.types.get_revocation_status_request
    import aws_sdk_signer.types.get_revocation_status_response
    import aws_sdk_signer.types.get_signing_platform_request
    import aws_sdk_signer.types.get_signing_platform_response
    import aws_sdk_signer.types.get_signing_profile_request
    import aws_sdk_signer.types.get_signing_profile_response
    import aws_sdk_signer.types.job_id
    import aws_sdk_signer.types.list_profile_permissions_request
    import aws_sdk_signer.types.list_profile_permissions_response
    import aws_sdk_signer.types.list_signing_jobs_request
    import aws_sdk_signer.types.list_signing_jobs_response
    import aws_sdk_signer.types.list_signing_platforms_request
    import aws_sdk_signer.types.list_signing_platforms_response
    import aws_sdk_signer.types.list_signing_profiles_request
    import aws_sdk_signer.types.list_signing_profiles_response
    import aws_sdk_signer.types.list_tags_for_resource_request
    import aws_sdk_signer.types.list_tags_for_resource_response
    import aws_sdk_signer.types.max_results
    import aws_sdk_signer.types.next_token
    import aws_sdk_signer.types.payload
    import aws_sdk_signer.types.platform_id
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.profile_version
    import aws_sdk_signer.types.put_signing_profile_request
    import aws_sdk_signer.types.put_signing_profile_response
    import aws_sdk_signer.types.remove_profile_permission_request
    import aws_sdk_signer.types.remove_profile_permission_response
    import aws_sdk_signer.types.requested_by
    import aws_sdk_signer.types.revocation_reason_string
    import aws_sdk_signer.types.revoke_signature_request
    import aws_sdk_signer.types.revoke_signing_profile_request
    import aws_sdk_signer.types.sign_payload_request
    import aws_sdk_signer.types.sign_payload_response
    import aws_sdk_signer.types.signature_validity_period
    import aws_sdk_signer.types.signing_material
    import aws_sdk_signer.types.signing_parameters
    import aws_sdk_signer.types.signing_platform_overrides
    import aws_sdk_signer.types.signing_status
    import aws_sdk_signer.types.source
    import aws_sdk_signer.types.start_signing_job_request
    import aws_sdk_signer.types.start_signing_job_response
    import aws_sdk_signer.types.statuses
    import aws_sdk_signer.types.string
    import aws_sdk_signer.types.tag_key_list
    import aws_sdk_signer.types.tag_map
    import aws_sdk_signer.types.tag_resource_request
    import aws_sdk_signer.types.tag_resource_response
    import aws_sdk_signer.types.timestamp
    import aws_sdk_signer.types.untag_resource_request
    import aws_sdk_signer.types.untag_resource_response


class signerClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class signerClient:
    """A client for the ``signer`` service.

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
        self._config = signerClientConfig(
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
        self, config_overrides: Optional[signerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: signerClientConfig = config_overrides or {}
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

    def add_profile_permission(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        action: "aws_sdk_signer.types.string.String",
        principal: "aws_sdk_signer.types.string.String",
        statement_id: "aws_sdk_signer.types.string.String",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        profile_version: Optional[
            "aws_sdk_signer.types.profile_version.ProfileVersion"
        ] = None,
        revision_id: Optional["aws_sdk_signer.types.string.String"] = None,
    ) -> "aws_sdk_signer.types.add_profile_permission_response.AddProfilePermissionResponse":
        r"""<p>Adds cross-account permissions to a signing profile.</p>

        Args:
            profile_name: <p>The human-readable name of the signing profile.</p>
            profile_version: <p>The version of the signing profile.</p>
            action: <p>For cross-account signing. Grant a designated account permission to perform one or more of the following actions. Each action is associated with a specific API's operations. For more information about cross-account signing, see <a href=\"http://docs.aws.amazon.com/signer/latest/developerguide/signing-profile-cross-account.html\">Using cross-account signing with signing profiles</a> in the <i>AWS Signer Developer Guide</i>.</p> <p>You can designate the following actions to an account.</p> <ul> <li> <p> <code>signer:StartSigningJob</code>. This action isn't supported for container image workflows. For details, see <a>StartSigningJob</a>.</p> </li> <li> <p> <code>signer:SignPayload</code>. This action isn't supported for AWS Lambda workflows. For details, see <a>SignPayload</a> </p> </li> <li> <p> <code>signer:GetSigningProfile</code>. For details, see <a>GetSigningProfile</a>.</p> </li> <li> <p> <code>signer:RevokeSignature</code>. For details, see <a>RevokeSignature</a>.</p> </li> </ul>
            principal: <p>The AWS principal receiving cross-account permissions. This may be an IAM role or another AWS account ID.</p>
            revision_id: <p>A unique identifier for the current profile revision.</p>
            statement_id: <p>A unique identifier for the cross-account permission statement.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.conflict_exception.ConflictException: <p>The resource encountered a conflicting state.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The client is making a request that exceeds service limits.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.add_profile_permission_request.AddProfilePermissionRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.add_profile_permission_response.AddProfilePermissionResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.add_profile_permission

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.add_profile_permission.add_profile_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.add_profile_permission_request.AddProfilePermissionRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        if profile_version is not None:
            input_["profile_version"] = profile_version
        input_["action"] = action
        input_["principal"] = principal
        if revision_id is not None:
            input_["revision_id"] = revision_id
        input_["statement_id"] = statement_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_signing_profile(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> None:
        r"""<p>Changes the state of an <code>ACTIVE</code> signing profile to <code>CANCELED</code>. A canceled profile is still viewable with the <code>ListSigningProfiles</code> operation, but it cannot perform new signing jobs. See <a href=\"https://docs.aws.amazon.com/signer/latest/developerguide/retention.html\">Data Retention</a> for more information on scheduled deletion of a canceled signing profile.</p>

        Args:
            profile_name: <p>The name of the signing profile to be canceled.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.cancel_signing_profile_request.CancelSigningProfileRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_signer._operations.wallaby_service.cancel_signing_profile

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.cancel_signing_profile.cancel_signing_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.cancel_signing_profile_request.CancelSigningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_signing_job(
        self,
        job_id: "aws_sdk_signer.types.job_id.JobId",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> (
        "aws_sdk_signer.types.describe_signing_job_response.DescribeSigningJobResponse"
    ):
        """<p>Returns information about a specific code signing job. You specify the job by using the <code>jobId</code> value that is returned by the <a>StartSigningJob</a> operation. </p>

        Args:
            job_id: <p>The ID of the signing job on input.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.describe_signing_job_request.DescribeSigningJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.describe_signing_job_response.DescribeSigningJobResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.describe_signing_job

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.describe_signing_job.describe_signing_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.describe_signing_job_request.DescribeSigningJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_revocation_status(
        self,
        signature_timestamp: "aws_sdk_signer.types.timestamp.Timestamp",
        platform_id: "aws_sdk_signer.types.platform_id.PlatformId",
        profile_version_arn: "aws_sdk_signer.types.arn.Arn",
        job_arn: "aws_sdk_signer.types.arn.Arn",
        certificate_hashes: "aws_sdk_signer.types.certificate_hashes.CertificateHashes",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> "aws_sdk_signer.types.get_revocation_status_response.GetRevocationStatusResponse":
        r"""<p>Retrieves the revocation status of one or more of the signing profile, signing job, and signing certificate.</p>

        Args:
            signature_timestamp: <p>The timestamp of the signature that validates the profile or job.</p>
            platform_id: <p>The ID of a signing platform. </p>
            profile_version_arn: <p>The version of a signing profile.</p>
            job_arn: <p>The ARN of a signing job.</p>
            certificate_hashes: <p>A list of composite signed hashes that identify certificates.</p> <p>A certificate identifier consists of a subject certificate TBS hash (signed by the parent CA) combined with a parent CA TBS hash (signed by the parent CA’s CA). Root certificates are defined as their own CA.</p> <p>The following example shows how to calculate a hash for this parameter using OpenSSL commands: </p> <p> <code>openssl asn1parse -in childCert.pem -strparse 4 -out childCert.tbs</code> </p> <p> <code>openssl sha384 < childCert.tbs -binary > childCertTbsHash</code> </p> <p> <code>openssl asn1parse -in parentCert.pem -strparse 4 -out parentCert.tbs</code> </p> <p> <code>openssl sha384 < parentCert.tbs -binary > parentCertTbsHash xxd -p childCertTbsHash > certificateHash.hex xxd -p parentCertTbsHash >> certificateHash.hex</code> </p> <p> <code>cat certificateHash.hex | tr -d '\n'</code> </p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.get_revocation_status_request.GetRevocationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.get_revocation_status_response.GetRevocationStatusResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.get_revocation_status

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.get_revocation_status.get_revocation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.get_revocation_status_request.GetRevocationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["signature_timestamp"] = signature_timestamp
        input_["platform_id"] = platform_id
        input_["profile_version_arn"] = profile_version_arn
        input_["job_arn"] = job_arn
        input_["certificate_hashes"] = certificate_hashes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_signing_platform(
        self,
        platform_id: "aws_sdk_signer.types.platform_id.PlatformId",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> (
        "aws_sdk_signer.types.get_signing_platform_response.GetSigningPlatformResponse"
    ):
        """<p>Returns information on a specific signing platform.</p>

        Args:
            platform_id: <p>The ID of the target signing platform.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.get_signing_platform_request.GetSigningPlatformRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.get_signing_platform_response.GetSigningPlatformResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.get_signing_platform

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.get_signing_platform.get_signing_platform(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.get_signing_platform_request.GetSigningPlatformRequest = {}  # type: ignore[typeddict-item]
        input_["platform_id"] = platform_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_signing_profile(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        profile_owner: Optional["aws_sdk_signer.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_signer.types.get_signing_profile_response.GetSigningProfileResponse":
        """<p>Returns information on a specific signing profile.</p>

        Args:
            profile_name: <p>The name of the target signing profile.</p>
            profile_owner: <p>The AWS account ID of the profile owner.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.get_signing_profile_request.GetSigningProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.get_signing_profile_response.GetSigningProfileResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.get_signing_profile

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.get_signing_profile.get_signing_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.get_signing_profile_request.GetSigningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        if profile_owner is not None:
            input_["profile_owner"] = profile_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_profile_permissions(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        next_token: Optional["aws_sdk_signer.types.string.String"] = None,
    ) -> "aws_sdk_signer.types.list_profile_permissions_response.ListProfilePermissionsResponse":
        """<p>Lists the cross-account permissions associated with a signing profile.</p>

        Args:
            profile_name: <p>Name of the signing profile containing the cross-account permissions.</p>
            next_token: <p>String for specifying the next set of paginated results.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.list_profile_permissions_request.ListProfilePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.list_profile_permissions_response.ListProfilePermissionsResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.list_profile_permissions

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.list_profile_permissions.list_profile_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.list_profile_permissions_request.ListProfilePermissionsRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_signing_jobs(
        self,
        *,
        config_overrides: Optional[signerClientConfig] = None,
        status: Optional["aws_sdk_signer.types.signing_status.SigningStatus"] = None,
        platform_id: Optional["aws_sdk_signer.types.platform_id.PlatformId"] = None,
        requested_by: Optional["aws_sdk_signer.types.requested_by.RequestedBy"] = None,
        max_results: Optional["aws_sdk_signer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_signer.types.next_token.NextToken"] = None,
        is_revoked: Optional["aws_sdk_signer.types.bool.bool"] = None,
        signature_expires_before: Optional[
            "aws_sdk_signer.types.timestamp.Timestamp"
        ] = None,
        signature_expires_after: Optional[
            "aws_sdk_signer.types.timestamp.Timestamp"
        ] = None,
        job_invoker: Optional["aws_sdk_signer.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_signer.types.list_signing_jobs_response.ListSigningJobsResponse":
        """<p>Lists all your signing jobs. You can use the <code>maxResults</code> parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, AWS Signer returns a <code>nextToken</code> value. Use this value in subsequent calls to <code>ListSigningJobs</code> to fetch the remaining values. You can continue calling <code>ListSigningJobs</code> with your <code>maxResults</code> parameter and with new values that Signer returns in the <code>nextToken</code> parameter until all of your signing jobs have been returned. </p>

        Args:
            status: <p>A status value with which to filter your results.</p>
            platform_id: <p>The ID of microcontroller platform that you specified for the distribution of your code image.</p>
            requested_by: <p>The IAM principal that requested the signing job.</p>
            max_results: <p>Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the <code>nextToken</code> element is set in the response. Use the <code>nextToken</code> value in a subsequent request to retrieve additional items. </p>
            next_token: <p>String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.</p>
            is_revoked: <p>Filters results to return only signing jobs with revoked signatures.</p>
            signature_expires_before: <p>Filters results to return only signing jobs with signatures expiring before a specified timestamp.</p>
            signature_expires_after: <p>Filters results to return only signing jobs with signatures expiring after a specified timestamp.</p>
            job_invoker: <p>Filters results to return only signing jobs initiated by a specified IAM entity.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.list_signing_jobs_request.ListSigningJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.list_signing_jobs_response.ListSigningJobsResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.list_signing_jobs

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.list_signing_jobs.list_signing_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.list_signing_jobs_request.ListSigningJobsRequest = {}  # type: ignore[typeddict-item]
        if status is not None:
            input_["status"] = status
        if platform_id is not None:
            input_["platform_id"] = platform_id
        if requested_by is not None:
            input_["requested_by"] = requested_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if is_revoked is not None:
            input_["is_revoked"] = is_revoked
        if signature_expires_before is not None:
            input_["signature_expires_before"] = signature_expires_before
        if signature_expires_after is not None:
            input_["signature_expires_after"] = signature_expires_after
        if job_invoker is not None:
            input_["job_invoker"] = job_invoker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_signing_platforms(
        self,
        *,
        config_overrides: Optional[signerClientConfig] = None,
        category: Optional["aws_sdk_signer.types.string.String"] = None,
        partner: Optional["aws_sdk_signer.types.string.String"] = None,
        target: Optional["aws_sdk_signer.types.string.String"] = None,
        max_results: Optional["aws_sdk_signer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_signer.types.string.String"] = None,
    ) -> "aws_sdk_signer.types.list_signing_platforms_response.ListSigningPlatformsResponse":
        """<p>Lists all signing platforms available in AWS Signer that match the request parameters. If additional jobs remain to be listed, Signer returns a <code>nextToken</code> value. Use this value in subsequent calls to <code>ListSigningJobs</code> to fetch the remaining values. You can continue calling <code>ListSigningJobs</code> with your <code>maxResults</code> parameter and with new values that Signer returns in the <code>nextToken</code> parameter until all of your signing jobs have been returned.</p>

        Args:
            category: <p>The category type of a signing platform.</p>
            partner: <p>Any partner entities connected to a signing platform.</p>
            target: <p>The validation template that is used by the target signing platform.</p>
            max_results: <p>The maximum number of results to be returned by this operation.</p>
            next_token: <p>Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.list_signing_platforms_request.ListSigningPlatformsRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.list_signing_platforms_response.ListSigningPlatformsResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.list_signing_platforms

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.list_signing_platforms.list_signing_platforms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.list_signing_platforms_request.ListSigningPlatformsRequest = {}  # type: ignore[typeddict-item]
        if category is not None:
            input_["category"] = category
        if partner is not None:
            input_["partner"] = partner
        if target is not None:
            input_["target"] = target
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

    def list_signing_profiles(
        self,
        *,
        config_overrides: Optional[signerClientConfig] = None,
        include_canceled: Optional["aws_sdk_signer.types.bool.bool"] = None,
        max_results: Optional["aws_sdk_signer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_signer.types.next_token.NextToken"] = None,
        platform_id: Optional["aws_sdk_signer.types.platform_id.PlatformId"] = None,
        statuses: Optional["aws_sdk_signer.types.statuses.Statuses"] = None,
    ) -> "aws_sdk_signer.types.list_signing_profiles_response.ListSigningProfilesResponse":
        """<p>Lists all available signing profiles in your AWS account. Returns only profiles with an <code>ACTIVE</code> status unless the <code>includeCanceled</code> request field is set to <code>true</code>. If additional jobs remain to be listed, AWS Signer returns a <code>nextToken</code> value. Use this value in subsequent calls to <code>ListSigningJobs</code> to fetch the remaining values. You can continue calling <code>ListSigningJobs</code> with your <code>maxResults</code> parameter and with new values that Signer returns in the <code>nextToken</code> parameter until all of your signing jobs have been returned.</p>

        Args:
            include_canceled: <p>Designates whether to include profiles with the status of <code>CANCELED</code>.</p>
            max_results: <p>The maximum number of profiles to be returned.</p>
            next_token: <p>Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.</p>
            platform_id: <p>Filters results to return only signing jobs initiated for a specified signing platform.</p>
            statuses: <p>Filters results to return only signing jobs with statuses in the specified list.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.list_signing_profiles_request.ListSigningProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.list_signing_profiles_response.ListSigningProfilesResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.list_signing_profiles

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.list_signing_profiles.list_signing_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.list_signing_profiles_request.ListSigningProfilesRequest = {}  # type: ignore[typeddict-item]
        if include_canceled is not None:
            input_["include_canceled"] = include_canceled
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if platform_id is not None:
            input_["platform_id"] = platform_id
        if statuses is not None:
            input_["statuses"] = statuses

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_signer.types.string.String",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> "aws_sdk_signer.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags associated with a signing profile resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the signing profile.</p>

        Raises:
            aws_sdk_signer.errors.bad_request_exception.BadRequestException: <p>The request contains invalid parameters for the ARN or tags. This exception also occurs when you call a tagging API on a cancelled signing profile.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.not_found_exception.NotFoundException: <p>The signing profile was not found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_signing_profile(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        platform_id: "aws_sdk_signer.types.platform_id.PlatformId",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        signing_material: Optional[
            "aws_sdk_signer.types.signing_material.SigningMaterial"
        ] = None,
        signature_validity_period: Optional[
            "aws_sdk_signer.types.signature_validity_period.SignatureValidityPeriod"
        ] = None,
        overrides: Optional[
            "aws_sdk_signer.types.signing_platform_overrides.SigningPlatformOverrides"
        ] = None,
        signing_parameters: Optional[
            "aws_sdk_signer.types.signing_parameters.SigningParameters"
        ] = None,
        tags: Optional["aws_sdk_signer.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_signer.types.put_signing_profile_response.PutSigningProfileResponse":
        """<p>Creates a signing profile. A signing profile is a code-signing template that can be used to carry out a pre-defined signing job. </p>

        Args:
            profile_name: <p>The name of the signing profile to be created.</p>
            signing_material: <p>The AWS Certificate Manager certificate that will be used to sign code with the new signing profile.</p>
            signature_validity_period: <p>The default validity period override for any signature generated using this signing profile. If unspecified, the default is 135 months.</p>
            platform_id: <p>The ID of the signing platform to be created.</p>
            overrides: <p>A subfield of <code>platform</code>. This specifies any different configuration options that you want to apply to the chosen platform (such as a different <code>hash-algorithm</code> or <code>signing-algorithm</code>).</p>
            signing_parameters: <p>Map of key-value pairs for signing. These can include any information that you want to use during signing.</p>
            tags: <p>Tags to be associated with the signing profile that is being created.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.put_signing_profile_request.PutSigningProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.put_signing_profile_response.PutSigningProfileResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.put_signing_profile

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.put_signing_profile.put_signing_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.put_signing_profile_request.PutSigningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        if signing_material is not None:
            input_["signing_material"] = signing_material
        if signature_validity_period is not None:
            input_["signature_validity_period"] = signature_validity_period
        input_["platform_id"] = platform_id
        if overrides is not None:
            input_["overrides"] = overrides
        if signing_parameters is not None:
            input_["signing_parameters"] = signing_parameters
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_profile_permission(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        revision_id: "aws_sdk_signer.types.string.String",
        statement_id: "aws_sdk_signer.types.string.String",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> "aws_sdk_signer.types.remove_profile_permission_response.RemoveProfilePermissionResponse":
        """<p>Removes cross-account permissions from a signing profile.</p>

        Args:
            profile_name: <p>A human-readable name for the signing profile with permissions to be removed.</p>
            revision_id: <p>An identifier for the current revision of the signing profile permissions.</p>
            statement_id: <p>A unique identifier for the cross-account permissions statement.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.conflict_exception.ConflictException: <p>The resource encountered a conflicting state.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.remove_profile_permission_request.RemoveProfilePermissionRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.remove_profile_permission_response.RemoveProfilePermissionResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.remove_profile_permission

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.remove_profile_permission.remove_profile_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.remove_profile_permission_request.RemoveProfilePermissionRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        input_["revision_id"] = revision_id
        input_["statement_id"] = statement_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def revoke_signature(
        self,
        job_id: "aws_sdk_signer.types.job_id.JobId",
        reason: "aws_sdk_signer.types.revocation_reason_string.RevocationReasonString",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        job_owner: Optional["aws_sdk_signer.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Changes the state of a signing job to <code>REVOKED</code>. This indicates that the signature is no longer valid.</p>

        Args:
            job_id: <p>ID of the signing job to be revoked.</p>
            job_owner: <p>AWS account ID of the job owner.</p>
            reason: <p>The reason for revoking the signing job.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.revoke_signature_request.RevokeSignatureRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_signer._operations.wallaby_service.revoke_signature

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.revoke_signature.revoke_signature(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.revoke_signature_request.RevokeSignatureRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        if job_owner is not None:
            input_["job_owner"] = job_owner
        input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def revoke_signing_profile(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        profile_version: "aws_sdk_signer.types.profile_version.ProfileVersion",
        reason: "aws_sdk_signer.types.revocation_reason_string.RevocationReasonString",
        effective_time: "aws_sdk_signer.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> None:
        r"""<p>Changes the state of a signing profile to <code>REVOKED</code>. This indicates that signatures generated using the signing profile after an effective start date are no longer valid. A revoked profile is still viewable with the <code>ListSigningProfiles</code> operation, but it cannot perform new signing jobs. See <a href=\"https://docs.aws.amazon.com/signer/latest/developerguide/retention.html\">Data Retention</a> for more information on scheduled deletion of a revoked signing profile. </p>

        Args:
            profile_name: <p>The name of the signing profile to be revoked.</p>
            profile_version: <p>The version of the signing profile to be revoked.</p>
            reason: <p>The reason for revoking a signing profile.</p>
            effective_time: <p>A timestamp for when revocation of a Signing Profile should become effective. Signatures generated using the signing profile after this timestamp are not trusted.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.revoke_signing_profile_request.RevokeSigningProfileRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_signer._operations.wallaby_service.revoke_signing_profile

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.revoke_signing_profile.revoke_signing_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.revoke_signing_profile_request.RevokeSigningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        input_["profile_version"] = profile_version
        input_["reason"] = reason
        input_["effective_time"] = effective_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def sign_payload(
        self,
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        payload: "aws_sdk_signer.types.payload.Payload",
        payload_format: "aws_sdk_signer.types.string.String",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        profile_owner: Optional["aws_sdk_signer.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_signer.types.sign_payload_response.SignPayloadResponse":
        """<p>Signs a binary payload and returns a signature envelope.</p>

        Args:
            profile_name: <p>The name of the signing profile.</p>
            profile_owner: <p>The AWS account ID of the profile owner.</p>
            payload: <p>Specifies the object digest (hash) to sign.</p>
            payload_format: <p>Payload content type. The single valid type is <code>application/vnd.cncf.notary.payload.v1+json</code>.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.sign_payload_request.SignPayloadRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.sign_payload_response.SignPayloadResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.sign_payload

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.sign_payload.sign_payload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.sign_payload_request.SignPayloadRequest = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        if profile_owner is not None:
            input_["profile_owner"] = profile_owner
        input_["payload"] = payload
        input_["payload_format"] = payload_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_signing_job(
        self,
        source: "aws_sdk_signer.types.source.Source",
        destination: "aws_sdk_signer.types.destination.Destination",
        profile_name: "aws_sdk_signer.types.profile_name.ProfileName",
        client_request_token: "aws_sdk_signer.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[signerClientConfig] = None,
        profile_owner: Optional["aws_sdk_signer.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_signer.types.start_signing_job_response.StartSigningJobResponse":
        r"""<p>Initiates a signing job to be performed on the code provided. Signing jobs are viewable by the <code>ListSigningJobs</code> operation. Note the following requirements: </p> <ul> <li> <p> You must create an Amazon S3 source bucket. For more information, see <a href=\"http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html\">Creating a Bucket</a> in the <i>Amazon S3 Getting Started Guide</i>. </p> </li> <li> <p>Your S3 source bucket must be version enabled.</p> </li> <li> <p>You must create an S3 destination bucket. AWS Signer uses your S3 destination bucket to write your signed code.</p> </li> <li> <p>You specify the name of the source and destination buckets when calling the <code>StartSigningJob</code> operation.</p> </li> <li> <p>You must ensure the S3 buckets are from the same Region as the signing profile. Cross-Region signing isn't supported.</p> </li> <li> <p>You must also specify a request token that identifies your request to Signer.</p> </li> </ul> <p>You can call the <a>DescribeSigningJob</a> and the <a>ListSigningJobs</a> actions after you call <code>StartSigningJob</code>.</p> <p>For a Java example that shows how to use this action, see <a href=\"https://docs.aws.amazon.com/signer/latest/developerguide/api-startsigningjob.html\">StartSigningJob</a>.</p>

        Args:
            source: <p>The S3 bucket that contains the object to sign or a BLOB that contains your raw code.</p>
            destination: <p>The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.</p>
            profile_name: <p>The name of the signing profile.</p>
            client_request_token: <p>String that identifies the signing request. All calls after the first that use this token return the same response as the first call.</p>
            profile_owner: <p>The AWS account ID of the signing profile owner.</p>

        Raises:
            aws_sdk_signer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be found.</p>
            aws_sdk_signer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p> <p>Instead of this error, <code>TooManyRequestsException</code> should be used.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.validation_exception.ValidationException: <p>You signing certificate could not be validated.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.start_signing_job_request.StartSigningJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.start_signing_job_response.StartSigningJobResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.start_signing_job

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.start_signing_job.start_signing_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.start_signing_job_request.StartSigningJobRequest = {}  # type: ignore[typeddict-item]
        input_["source"] = source
        input_["destination"] = destination
        input_["profile_name"] = profile_name
        input_["client_request_token"] = client_request_token
        if profile_owner is not None:
            input_["profile_owner"] = profile_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_signer.types.string.String",
        tags: "aws_sdk_signer.types.tag_map.TagMap",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> "aws_sdk_signer.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to a signing profile. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value. To specify the signing profile, use its Amazon Resource Name (ARN). To specify the tag, use a key-value pair.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the signing profile.</p>
            tags: <p>One or more tags to be associated with the signing profile.</p>

        Raises:
            aws_sdk_signer.errors.bad_request_exception.BadRequestException: <p>The request contains invalid parameters for the ARN or tags. This exception also occurs when you call a tagging API on a cancelled signing profile.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.not_found_exception.NotFoundException: <p>The signing profile was not found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.tag_resource

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_signer.types.string.String",
        tag_keys: "aws_sdk_signer.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[signerClientConfig] = None,
    ) -> "aws_sdk_signer.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a signing profile. To remove the tags, specify a list of tag keys.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the signing profile.</p>
            tag_keys: <p>A list of tag keys to be removed from the signing profile.</p>

        Raises:
            aws_sdk_signer.errors.bad_request_exception.BadRequestException: <p>The request contains invalid parameters for the ARN or tags. This exception also occurs when you call a tagging API on a cancelled signing profile.</p>
            aws_sdk_signer.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error occurred.</p>
            aws_sdk_signer.errors.not_found_exception.NotFoundException: <p>The signing profile was not found.</p>
            aws_sdk_signer.errors.too_many_requests_exception.TooManyRequestsException: <p>The allowed number of job-signing requests has been exceeded.</p> <p>This error supersedes the error <code>ThrottlingException</code>.</p>
            aws_sdk_signer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_signer._operations.wallaby_service.untag_resource

            output, http_response = (
                aws_sdk_signer._operations.wallaby_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
