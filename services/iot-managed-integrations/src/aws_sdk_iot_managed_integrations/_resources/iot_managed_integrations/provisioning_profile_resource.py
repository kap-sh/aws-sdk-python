from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ca_certificate
    import aws_sdk_iot_managed_integrations.types.claim_certificate
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.create_provisioning_profile_request
    import aws_sdk_iot_managed_integrations.types.create_provisioning_profile_response
    import aws_sdk_iot_managed_integrations.types.delete_provisioning_profile_request
    import aws_sdk_iot_managed_integrations.types.get_provisioning_profile_request
    import aws_sdk_iot_managed_integrations.types.get_provisioning_profile_response
    import aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_request
    import aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_id
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_name
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_summary
    import aws_sdk_iot_managed_integrations.types.provisioning_type
    import aws_sdk_iot_managed_integrations.types.tags_map
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ProvisioningProfileResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        provisioning_type: "aws_sdk_iot_managed_integrations.types.provisioning_type.ProvisioningType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        ca_certificate: Optional[
            "aws_sdk_iot_managed_integrations.types.ca_certificate.CaCertificate"
        ] = None,
        claim_certificate: Optional[
            "aws_sdk_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse":
        """<p>Create a provisioning profile for executing device provisioning flows. The provisioning profile is a document that defines the set of resources and policies applied to a device during the provisioning process.</p>

        Args:
            provisioning_type: <p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>
            ca_certificate: <p>The body of the PEM-encoded certificate authority (CA) certificate.</p>
            claim_certificate: <p>The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.</p>
            name: <p>The name of the provisioning profile.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the provisioning profile.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile.create_provisioning_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["provisioning_type"] = provisioning_type
        if ca_certificate is not None:
            input_["ca_certificate"] = ca_certificate
        if claim_certificate is not None:
            input_["claim_certificate"] = claim_certificate
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

    def read(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse":
        """<p>Get details of a provisioning profile.</p>

        Args:
            identifier: <p>The id of a provisioning profile.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile.get_provisioning_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a provisioning profile.</p>

        Args:
            identifier: <p>The id of the provisioning profile.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile.delete_provisioning_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse":
        """<p>List the provisioning profiles within the Amazon Web Services account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles.list_provisioning_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncProvisioningProfileResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        provisioning_type: "aws_sdk_iot_managed_integrations.types.provisioning_type.ProvisioningType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        ca_certificate: Optional[
            "aws_sdk_iot_managed_integrations.types.ca_certificate.CaCertificate"
        ] = None,
        claim_certificate: Optional[
            "aws_sdk_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse":
        """<p>Create a provisioning profile for executing device provisioning flows. The provisioning profile is a document that defines the set of resources and policies applied to a device during the provisioning process.</p>

        Args:
            provisioning_type: <p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>
            ca_certificate: <p>The body of the PEM-encoded certificate authority (CA) certificate.</p>
            claim_certificate: <p>The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.</p>
            name: <p>The name of the provisioning profile.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the provisioning profile.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile.async_create_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["provisioning_type"] = provisioning_type
        if ca_certificate is not None:
            input_["ca_certificate"] = ca_certificate
        if claim_certificate is not None:
            input_["claim_certificate"] = claim_certificate
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse":
        """<p>Get details of a provisioning profile.</p>

        Args:
            identifier: <p>The id of a provisioning profile.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile.async_get_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a provisioning profile.</p>

        Args:
            identifier: <p>The id of the provisioning profile.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile.async_delete_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse":
        """<p>List the provisioning profiles within the Amazon Web Services account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles.async_list_provisioning_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest = {}  # type: ignore[typeddict-item]
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
