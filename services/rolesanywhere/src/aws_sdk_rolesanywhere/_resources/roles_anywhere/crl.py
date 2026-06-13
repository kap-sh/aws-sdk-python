from typing import TYPE_CHECKING, Optional

import aws_sdk_rolesanywhere._auth._signers
import aws_sdk_rolesanywhere._auth._sigv4
from aws_sdk_rolesanywhere._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.crl_detail
    import aws_sdk_rolesanywhere.types.crl_detail_response
    import aws_sdk_rolesanywhere.types.import_crl_request
    import aws_sdk_rolesanywhere.types.list_crls_response
    import aws_sdk_rolesanywhere.types.list_request
    import aws_sdk_rolesanywhere.types.resource_name
    import aws_sdk_rolesanywhere.types.scalar_crl_request
    import aws_sdk_rolesanywhere.types.tag_list
    import aws_sdk_rolesanywhere.types.trust_anchor_arn
    import aws_sdk_rolesanywhere.types.update_crl_request
    import aws_sdk_rolesanywhere.types.uuid
    from aws_sdk_rolesanywhere._services.async_roles_anywhere import (
        AsyncRolesAnywhereClient,
        AsyncRolesAnywhereClientConfig,
    )
    from aws_sdk_rolesanywhere._services.roles_anywhere import (
        RolesAnywhereClient,
        RolesAnywhereClientConfig,
    )


class Crl:
    def __init__(self, service: RolesAnywhereClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_rolesanywhere.types.resource_name.ResourceName",
        crl_data: bytes,
        trust_anchor_arn: "aws_sdk_rolesanywhere.types.trust_anchor_arn.TrustAnchorArn",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_rolesanywhere.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Imports the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA).In order to be properly imported, a CRL must be in PEM format. IAM Roles Anywhere validates against the CRL before issuing credentials. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ImportCrl</code>. </p>

        Args:
            name: <p>The name of the certificate revocation list (CRL).</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
            enabled: <p>Specifies whether the certificate revocation list (CRL) is enabled.</p>
            tags: <p>A list of tags to attach to the certificate revocation list (CRL).</p>
            trust_anchor_arn: <p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.import_crl_request.ImportCrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.import_crl

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.import_crl.import_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.import_crl_request.ImportCrlRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["crl_data"] = crl_data
        if enabled is not None:
            input["enabled"] = enabled
        if tags is not None:
            input["tags"] = tags
        input["trust_anchor_arn"] = trust_anchor_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Gets a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_crl

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.get_crl.get_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        name: Optional["aws_sdk_rolesanywhere.types.resource_name.ResourceName"] = None,
        crl_data: Optional[bytes] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Updates the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
            name: <p>The name of the Crl.</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.update_crl_request.UpdateCrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.update_crl

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.update_crl.update_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.update_crl_request.UpdateCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id
        if name is not None:
            input["name"] = name
        if crl_data is not None:
            input["crl_data"] = crl_data

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Deletes a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_crl

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.delete_crl.delete_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_crls_response.ListCrlsResponse":
        """<p>Lists all certificate revocation lists (CRL) in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListCrls</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.list_crls_response.ListCrlsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_crls

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.list_crls.list_crls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.list_request.ListRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if page_size is not None:
            input["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_crl(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Disables a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.disable_crl

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.disable_crl.disable_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_crl(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Enables a certificate revocation list (CRL). When enabled, certificates stored in the CRL are unauthorized to receive session credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.enable_crl

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.enable_crl.enable_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCrl:
    def __init__(self, service: AsyncRolesAnywhereClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_rolesanywhere.types.resource_name.ResourceName",
        crl_data: bytes,
        trust_anchor_arn: "aws_sdk_rolesanywhere.types.trust_anchor_arn.TrustAnchorArn",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_rolesanywhere.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Imports the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA).In order to be properly imported, a CRL must be in PEM format. IAM Roles Anywhere validates against the CRL before issuing credentials. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ImportCrl</code>. </p>

        Args:
            name: <p>The name of the certificate revocation list (CRL).</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
            enabled: <p>Specifies whether the certificate revocation list (CRL) is enabled.</p>
            tags: <p>A list of tags to attach to the certificate revocation list (CRL).</p>
            trust_anchor_arn: <p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.import_crl_request.ImportCrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.import_crl

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.import_crl.async_import_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.import_crl_request.ImportCrlRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["crl_data"] = crl_data
        if enabled is not None:
            input["enabled"] = enabled
        if tags is not None:
            input["tags"] = tags
        input["trust_anchor_arn"] = trust_anchor_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Gets a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_crl

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.get_crl.async_get_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["aws_sdk_rolesanywhere.types.resource_name.ResourceName"] = None,
        crl_data: Optional[bytes] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Updates the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
            name: <p>The name of the Crl.</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.update_crl_request.UpdateCrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.update_crl

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.update_crl.async_update_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.update_crl_request.UpdateCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id
        if name is not None:
            input["name"] = name
        if crl_data is not None:
            input["crl_data"] = crl_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Deletes a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_crl

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.delete_crl.async_delete_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_crls_response.ListCrlsResponse":
        """<p>Lists all certificate revocation lists (CRL) in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListCrls</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.list_crls_response.ListCrlsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_crls

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.list_crls.async_list_crls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.list_request.ListRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if page_size is not None:
            input["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_crl(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Disables a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.disable_crl

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.disable_crl.async_disable_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_crl(
        self,
        crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Enables a certificate revocation list (CRL). When enabled, certificates stored in the CRL are unauthorized to receive session credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.enable_crl

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.enable_crl.async_enable_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {}  # type: ignore[typeddict-item]
        input["crl_id"] = crl_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
