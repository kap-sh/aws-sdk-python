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
    import aws_sdk_rolesanywhere.types.create_trust_anchor_request
    import aws_sdk_rolesanywhere.types.list_request
    import aws_sdk_rolesanywhere.types.list_trust_anchors_response
    import aws_sdk_rolesanywhere.types.notification_settings
    import aws_sdk_rolesanywhere.types.resource_name
    import aws_sdk_rolesanywhere.types.scalar_trust_anchor_request
    import aws_sdk_rolesanywhere.types.source
    import aws_sdk_rolesanywhere.types.tag_list
    import aws_sdk_rolesanywhere.types.trust_anchor_detail
    import aws_sdk_rolesanywhere.types.trust_anchor_detail_response
    import aws_sdk_rolesanywhere.types.update_trust_anchor_request
    import aws_sdk_rolesanywhere.types.uuid
    from aws_sdk_rolesanywhere._services.async_roles_anywhere import (
        AsyncRolesAnywhereClient,
        AsyncRolesAnywhereClientConfig,
    )
    from aws_sdk_rolesanywhere._services.roles_anywhere import (
        RolesAnywhereClient,
        RolesAnywhereClientConfig,
    )


class TrustAnchor:
    def __init__(self, service: RolesAnywhereClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_rolesanywhere.types.resource_name.ResourceName",
        source: "aws_sdk_rolesanywhere.types.source.Source",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_rolesanywhere.types.tag_list.TagList"] = None,
        notification_settings: Optional[
            "aws_sdk_rolesanywhere.types.notification_settings.NotificationSettings"
        ] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Creates a trust anchor to establish trust between IAM Roles Anywhere and your certificate authority (CA). You can define a trust anchor as a reference to an Private Certificate Authority (Private CA) or by uploading a CA certificate. Your Amazon Web Services workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary Amazon Web Services credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:CreateTrustAnchor</code>. </p>

        Args:
            name: <p>The name of the trust anchor.</p>
            source: <p>The trust anchor type and its related certificate data.</p>
            enabled: <p>Specifies whether the trust anchor is enabled.</p>
            tags: <p>The tags to attach to the trust anchor.</p>
            notification_settings: <p>A list of notification settings to be associated to the trust anchor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.create_trust_anchor_request.CreateTrustAnchorRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.create_trust_anchor

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.create_trust_anchor.create_trust_anchor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.create_trust_anchor_request.CreateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["source"] = source
        if enabled is not None:
            input["enabled"] = enabled
        if tags is not None:
            input["tags"] = tags
        if notification_settings is not None:
            input["notification_settings"] = notification_settings

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Gets a trust anchor.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_trust_anchor

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.get_trust_anchor.get_trust_anchor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        name: Optional["aws_sdk_rolesanywhere.types.resource_name.ResourceName"] = None,
        source: Optional["aws_sdk_rolesanywhere.types.source.Source"] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Updates a trust anchor. You establish trust between IAM Roles Anywhere and your certificate authority (CA) by configuring a trust anchor. You can define a trust anchor as a reference to an Private Certificate Authority (Private CA) or by uploading a CA certificate. Your Amazon Web Services workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary Amazon Web Services credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            name: <p>The name of the trust anchor.</p>
            source: <p>The trust anchor type and its related certificate data.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.update_trust_anchor_request.UpdateTrustAnchorRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.update_trust_anchor

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.update_trust_anchor.update_trust_anchor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.update_trust_anchor_request.UpdateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id
        if name is not None:
            input["name"] = name
        if source is not None:
            input["source"] = source

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Deletes a trust anchor.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_trust_anchor

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.delete_trust_anchor.delete_trust_anchor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

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
    ) -> "aws_sdk_rolesanywhere.types.list_trust_anchors_response.ListTrustAnchorsResponse":
        """<p>Lists the trust anchors in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListTrustAnchors</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.list_trust_anchors_response.ListTrustAnchorsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_trust_anchors

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.list_trust_anchors.list_trust_anchors(
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

    def disable_trust_anchor(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Disables a trust anchor. When disabled, temporary credential requests specifying this trust anchor are unauthorized.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.disable_trust_anchor

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.disable_trust_anchor.disable_trust_anchor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_trust_anchor(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Enables a trust anchor. When enabled, certificates in the trust anchor chain are authorized for trust validation. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.enable_trust_anchor

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.enable_trust_anchor.enable_trust_anchor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTrustAnchor:
    def __init__(self, service: AsyncRolesAnywhereClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_rolesanywhere.types.resource_name.ResourceName",
        source: "aws_sdk_rolesanywhere.types.source.Source",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_rolesanywhere.types.tag_list.TagList"] = None,
        notification_settings: Optional[
            "aws_sdk_rolesanywhere.types.notification_settings.NotificationSettings"
        ] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Creates a trust anchor to establish trust between IAM Roles Anywhere and your certificate authority (CA). You can define a trust anchor as a reference to an Private Certificate Authority (Private CA) or by uploading a CA certificate. Your Amazon Web Services workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary Amazon Web Services credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:CreateTrustAnchor</code>. </p>

        Args:
            name: <p>The name of the trust anchor.</p>
            source: <p>The trust anchor type and its related certificate data.</p>
            enabled: <p>Specifies whether the trust anchor is enabled.</p>
            tags: <p>The tags to attach to the trust anchor.</p>
            notification_settings: <p>A list of notification settings to be associated to the trust anchor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.create_trust_anchor_request.CreateTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.create_trust_anchor

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.create_trust_anchor.async_create_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.create_trust_anchor_request.CreateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["source"] = source
        if enabled is not None:
            input["enabled"] = enabled
        if tags is not None:
            input["tags"] = tags
        if notification_settings is not None:
            input["notification_settings"] = notification_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Gets a trust anchor.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_trust_anchor

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.get_trust_anchor.async_get_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["aws_sdk_rolesanywhere.types.resource_name.ResourceName"] = None,
        source: Optional["aws_sdk_rolesanywhere.types.source.Source"] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Updates a trust anchor. You establish trust between IAM Roles Anywhere and your certificate authority (CA) by configuring a trust anchor. You can define a trust anchor as a reference to an Private Certificate Authority (Private CA) or by uploading a CA certificate. Your Amazon Web Services workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary Amazon Web Services credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            name: <p>The name of the trust anchor.</p>
            source: <p>The trust anchor type and its related certificate data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.update_trust_anchor_request.UpdateTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.update_trust_anchor

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.update_trust_anchor.async_update_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.update_trust_anchor_request.UpdateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id
        if name is not None:
            input["name"] = name
        if source is not None:
            input["source"] = source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Deletes a trust anchor.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_trust_anchor

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.delete_trust_anchor.async_delete_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

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
    ) -> "aws_sdk_rolesanywhere.types.list_trust_anchors_response.ListTrustAnchorsResponse":
        """<p>Lists the trust anchors in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListTrustAnchors</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.list_trust_anchors_response.ListTrustAnchorsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_trust_anchors

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.list_trust_anchors.async_list_trust_anchors(
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

    async def disable_trust_anchor(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Disables a trust anchor. When disabled, temporary credential requests specifying this trust anchor are unauthorized.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.disable_trust_anchor

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.disable_trust_anchor.async_disable_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_trust_anchor(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Enables a trust anchor. When enabled, certificates in the trust anchor chain are authorized for trust validation. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.enable_trust_anchor

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.enable_trust_anchor.async_enable_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
        input["trust_anchor_id"] = trust_anchor_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
