from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_socialmessaging._auth._signers
import aws_sdk_socialmessaging._auth._sigv4
from aws_sdk_socialmessaging._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.associate_whats_app_business_account_input
    import aws_sdk_socialmessaging.types.associate_whats_app_business_account_output
    import aws_sdk_socialmessaging.types.create_whats_app_flow_input
    import aws_sdk_socialmessaging.types.create_whats_app_flow_output
    import aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_input
    import aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_output
    import aws_sdk_socialmessaging.types.create_whats_app_message_template_input
    import aws_sdk_socialmessaging.types.create_whats_app_message_template_media_input
    import aws_sdk_socialmessaging.types.create_whats_app_message_template_media_output
    import aws_sdk_socialmessaging.types.create_whats_app_message_template_output
    import aws_sdk_socialmessaging.types.delete_all_languages
    import aws_sdk_socialmessaging.types.delete_whats_app_flow_input
    import aws_sdk_socialmessaging.types.delete_whats_app_flow_output
    import aws_sdk_socialmessaging.types.delete_whats_app_message_template_input
    import aws_sdk_socialmessaging.types.delete_whats_app_message_template_output
    import aws_sdk_socialmessaging.types.deprecate_whats_app_flow_input
    import aws_sdk_socialmessaging.types.deprecate_whats_app_flow_output
    import aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_input
    import aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_output
    import aws_sdk_socialmessaging.types.filter
    import aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_input
    import aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_output
    import aws_sdk_socialmessaging.types.get_whats_app_flow_input
    import aws_sdk_socialmessaging.types.get_whats_app_flow_output
    import aws_sdk_socialmessaging.types.get_whats_app_flow_preview_input
    import aws_sdk_socialmessaging.types.get_whats_app_flow_preview_output
    import aws_sdk_socialmessaging.types.get_whats_app_message_template_input
    import aws_sdk_socialmessaging.types.get_whats_app_message_template_output
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_input
    import aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_output
    import aws_sdk_socialmessaging.types.list_whats_app_flow_assets_input
    import aws_sdk_socialmessaging.types.list_whats_app_flow_assets_output
    import aws_sdk_socialmessaging.types.list_whats_app_flows_input
    import aws_sdk_socialmessaging.types.list_whats_app_flows_output
    import aws_sdk_socialmessaging.types.list_whats_app_message_templates_input
    import aws_sdk_socialmessaging.types.list_whats_app_message_templates_output
    import aws_sdk_socialmessaging.types.list_whats_app_template_library_input
    import aws_sdk_socialmessaging.types.list_whats_app_template_library_output
    import aws_sdk_socialmessaging.types.max_results
    import aws_sdk_socialmessaging.types.meta_flow_category_list
    import aws_sdk_socialmessaging.types.meta_flow_id
    import aws_sdk_socialmessaging.types.meta_flow_json_blob
    import aws_sdk_socialmessaging.types.meta_flow_name
    import aws_sdk_socialmessaging.types.meta_library_template
    import aws_sdk_socialmessaging.types.meta_parameter_format
    import aws_sdk_socialmessaging.types.meta_template_category
    import aws_sdk_socialmessaging.types.meta_template_components
    import aws_sdk_socialmessaging.types.meta_template_cta_link_tracking_opted_out
    import aws_sdk_socialmessaging.types.meta_template_definition
    import aws_sdk_socialmessaging.types.meta_template_id
    import aws_sdk_socialmessaging.types.meta_template_language
    import aws_sdk_socialmessaging.types.meta_template_name
    import aws_sdk_socialmessaging.types.next_token
    import aws_sdk_socialmessaging.types.publish_whats_app_flow_input
    import aws_sdk_socialmessaging.types.publish_whats_app_flow_output
    import aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_input
    import aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_output
    import aws_sdk_socialmessaging.types.s3_file
    import aws_sdk_socialmessaging.types.update_whats_app_flow_assets_input
    import aws_sdk_socialmessaging.types.update_whats_app_flow_assets_output
    import aws_sdk_socialmessaging.types.update_whats_app_flow_input
    import aws_sdk_socialmessaging.types.update_whats_app_flow_output
    import aws_sdk_socialmessaging.types.update_whats_app_message_template_input
    import aws_sdk_socialmessaging.types.update_whats_app_message_template_output
    import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations
    import aws_sdk_socialmessaging.types.whats_app_setup_finalization
    import aws_sdk_socialmessaging.types.whats_app_signup_callback
    from aws_sdk_socialmessaging._services.async_social_messaging import (
        AsyncSocialMessagingClient,
        AsyncSocialMessagingClientConfig,
    )
    from aws_sdk_socialmessaging._services.social_messaging import (
        SocialMessagingClient,
        SocialMessagingClientConfig,
    )


class LinkedWhatsAppBusinessAccountResource:
    def __init__(self, service: SocialMessagingClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        signup_callback: Optional[
            "aws_sdk_socialmessaging.types.whats_app_signup_callback.WhatsAppSignupCallback"
        ] = None,
        setup_finalization: Optional[
            "aws_sdk_socialmessaging.types.whats_app_setup_finalization.WhatsAppSetupFinalization"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput":
        """<p>This is only used through the Amazon Web Services console during sign-up to associate your WhatsApp Business Account to your Amazon Web Services account.</p>

        Args:
            signup_callback: <p>Contains the callback access token.</p>
            setup_finalization: <p>A JSON object that contains the phone numbers and WhatsApp Business Account to link to your account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.associate_whats_app_business_account

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.associate_whats_app_business_account.associate_whats_app_business_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
        if signup_callback is not None:
            input_["signup_callback"] = signup_callback
        if setup_finalization is not None:
            input_["setup_finalization"] = setup_finalization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_output.GetLinkedWhatsAppBusinessAccountOutput":
        r"""<p>Get the details of your linked WhatsApp Business Account.</p>

        Args:
            id: <p>The unique identifier, from Amazon Web Services, of the linked WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html\">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_input.GetLinkedWhatsAppBusinessAccountInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_output.GetLinkedWhatsAppBusinessAccountOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account.get_linked_whats_app_business_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_input.GetLinkedWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_output.DisassociateWhatsAppBusinessAccountOutput":
        r"""<p>Disassociate a WhatsApp Business Account (WABA) from your Amazon Web Services account.</p>

        Args:
            id: <p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html\">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_input.DisassociateWhatsAppBusinessAccountInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_output.DisassociateWhatsAppBusinessAccountOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.disassociate_whats_app_business_account

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.disassociate_whats_app_business_account.disassociate_whats_app_business_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_input.DisassociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_output.ListLinkedWhatsAppBusinessAccountsOutput":
        """<p>List all WhatsApp Business Accounts linked to your Amazon Web Services account.</p>

        Args:
            next_token: <p>The next token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_input.ListLinkedWhatsAppBusinessAccountsInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_output.ListLinkedWhatsAppBusinessAccountsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_linked_whats_app_business_accounts

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.list_linked_whats_app_business_accounts.list_linked_whats_app_business_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_input.ListLinkedWhatsAppBusinessAccountsInput = {}  # type: ignore[typeddict-item]
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

    def create_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_name: "aws_sdk_socialmessaging.types.meta_flow_name.MetaFlowName",
        categories: "aws_sdk_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        flow_json: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob"
        ] = None,
        publish: Optional[bool] = None,
        clone_flow_id: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_flow_output.CreateWhatsAppFlowOutput":
        """<p>Creates a new WhatsApp Flow. Flows enable businesses to create rich, interactive forms and experiences that users can complete without leaving WhatsApp. The Flow is created in DRAFT status. If <code>publish</code> is set to <code>true</code> and a valid <code>flowJson</code> is provided, the Flow is published immediately.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to associate with this Flow.</p>
            flow_name: <p>The name of the Flow. Must be unique within the WhatsApp Business Account.</p>
            categories: <p>The categories that classify the business purpose of the Flow. At least one category is required.</p>
            flow_json: <p>The Flow JSON definition that describes the screens, components, and logic of the Flow. Maximum size is 10 MB.</p>
            publish: <p>Set to <code>true</code> to publish the Flow immediately after creation. Requires a valid <code>flowJson</code> that passes Meta's validation.</p>
            clone_flow_id: <p>The ID of an existing Flow within the same WhatsApp Business Account to clone.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.create_whats_app_flow_input.CreateWhatsAppFlowInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_flow_output.CreateWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_flow

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_flow.create_whats_app_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_flow_input.CreateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_name"] = flow_name
        input_["categories"] = categories
        if flow_json is not None:
            input_["flow_json"] = flow_json
        if publish is not None:
            input_["publish"] = publish
        if clone_flow_id is not None:
            input_["clone_flow_id"] = clone_flow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_whats_app_message_template(
        self,
        template_definition: "aws_sdk_socialmessaging.types.meta_template_definition.MetaTemplateDefinition",
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_message_template_output.CreateWhatsAppMessageTemplateOutput":
        """<p>Creates a new WhatsApp message template from a custom definition.</p> <note> <p>Amazon Web Services End User Messaging Social does not store any WhatsApp message template content.</p> </note>

        Args:
            template_definition: <p>The complete template definition as a JSON blob.</p>
            id: <p>The ID of the WhatsApp Business Account to associate with this template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.create_whats_app_message_template_input.CreateWhatsAppMessageTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_message_template_output.CreateWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template.create_whats_app_message_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_message_template_input.CreateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_definition"] = template_definition
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_whats_app_message_template_from_library(
        self,
        meta_library_template: "aws_sdk_socialmessaging.types.meta_library_template.MetaLibraryTemplate",
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_output.CreateWhatsAppMessageTemplateFromLibraryOutput":
        """<p>Creates a new WhatsApp message template using a template from Meta's template library.</p>

        Args:
            meta_library_template: <p>The template configuration from Meta's library, including customizations for buttons and body text.</p>
            id: <p>The ID of the WhatsApp Business Account to associate with this template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_input.CreateWhatsAppMessageTemplateFromLibraryInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_output.CreateWhatsAppMessageTemplateFromLibraryOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_from_library

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_from_library.create_whats_app_message_template_from_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_input.CreateWhatsAppMessageTemplateFromLibraryInput = {}  # type: ignore[typeddict-item]
        input_["meta_library_template"] = meta_library_template
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_whats_app_message_template_media(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        source_s3_file: Optional["aws_sdk_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_message_template_media_output.CreateWhatsAppMessageTemplateMediaOutput":
        """<p>Uploads media for use in a WhatsApp message template.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this media upload.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.create_whats_app_message_template_media_input.CreateWhatsAppMessageTemplateMediaInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_message_template_media_output.CreateWhatsAppMessageTemplateMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_media

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_media.create_whats_app_message_template_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_message_template_media_input.CreateWhatsAppMessageTemplateMediaInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.delete_whats_app_flow_output.DeleteWhatsAppFlowOutput":
        """<p>Deletes a WhatsApp Flow permanently. Only Flows in DRAFT status can be deleted. Published or deprecated Flows cannot be deleted.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.delete_whats_app_flow_input.DeleteWhatsAppFlowInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.delete_whats_app_flow_output.DeleteWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_flow

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_flow.delete_whats_app_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.delete_whats_app_flow_input.DeleteWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_whats_app_message_template(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        template_name: "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        delete_all_languages: Optional[
            "aws_sdk_socialmessaging.types.delete_all_languages.DeleteAllLanguages"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.delete_whats_app_message_template_output.DeleteWhatsAppMessageTemplateOutput":
        """<p>Deletes a WhatsApp message template.</p>

        Args:
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            delete_all_languages: <p>If true, deletes all language versions of the template.</p>
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            template_name: <p>The name of the template to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.delete_whats_app_message_template_input.DeleteWhatsAppMessageTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.delete_whats_app_message_template_output.DeleteWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_template

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_template.delete_whats_app_message_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.delete_whats_app_message_template_input.DeleteWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if delete_all_languages is not None:
            input_["delete_all_languages"] = delete_all_languages
        input_["id"] = id
        input_["template_name"] = template_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deprecate_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.deprecate_whats_app_flow_output.DeprecateWhatsAppFlowOutput":
        """<p>Deprecates a published WhatsApp Flow, marking it as no longer recommended for use. The Flow must be in PUBLISHED status. This is an irreversible operation.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to deprecate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.deprecate_whats_app_flow_input.DeprecateWhatsAppFlowInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.deprecate_whats_app_flow_output.DeprecateWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.deprecate_whats_app_flow

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.deprecate_whats_app_flow.deprecate_whats_app_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.deprecate_whats_app_flow_input.DeprecateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> (
        "aws_sdk_socialmessaging.types.get_whats_app_flow_output.GetWhatsAppFlowOutput"
    ):
        """<p>Retrieves the metadata and status of a WhatsApp Flow, including validation errors, preview information, and health status.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.get_whats_app_flow_input.GetWhatsAppFlowInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_flow_output.GetWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow.get_whats_app_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_flow_input.GetWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_whats_app_flow_preview(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        invalidate: Optional[bool] = None,
    ) -> "aws_sdk_socialmessaging.types.get_whats_app_flow_preview_output.GetWhatsAppFlowPreviewOutput":
        """<p>Generates a web preview URL for testing a WhatsApp Flow before publishing. Preview URLs expire in 30 days and can be shared with stakeholders for review.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to preview.</p>
            invalidate: <p>Set to <code>true</code> to force generation of a new preview URL. Use this if the previous URL has been compromised or you want a fresh expiration period.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.get_whats_app_flow_preview_input.GetWhatsAppFlowPreviewInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_flow_preview_output.GetWhatsAppFlowPreviewOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow_preview

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow_preview.get_whats_app_flow_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_flow_preview_input.GetWhatsAppFlowPreviewInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
        if invalidate is not None:
            input_["invalidate"] = invalidate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_whats_app_message_template(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        template_name: Optional[
            "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
        ] = None,
        template_language_code: Optional[
            "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.get_whats_app_message_template_output.GetWhatsAppMessageTemplateOutput":
        """<p>Retrieves a specific WhatsApp message template.</p>

        Args:
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            template_name: <p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            template_language_code: <p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.get_whats_app_message_template_input.GetWhatsAppMessageTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_message_template_output.GetWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_template

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_template.get_whats_app_message_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_message_template_input.GetWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        input_["id"] = id
        if template_name is not None:
            input_["template_name"] = template_name
        if template_language_code is not None:
            input_["template_language_code"] = template_language_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_whats_app_flow_assets(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_flow_assets_output.ListWhatsAppFlowAssetsOutput":
        """<p>Lists the assets (Flow JSON definition) of a WhatsApp Flow with presigned download URLs. Download URLs are generated by Meta and expire after a short period.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow whose assets to list.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.list_whats_app_flow_assets_input.ListWhatsAppFlowAssetsInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_flow_assets_output.ListWhatsAppFlowAssetsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flow_assets

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flow_assets.list_whats_app_flow_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_flow_assets_input.ListWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
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

    def list_whats_app_flows(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_flows_output.ListWhatsAppFlowsOutput":
        """<p>Lists all WhatsApp Flows for a WhatsApp Business Account. Returns summary information including Flow ID, name, status, and categories.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to list Flows for.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.list_whats_app_flows_input.ListWhatsAppFlowsInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_flows_output.ListWhatsAppFlowsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flows

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flows.list_whats_app_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_flows_input.ListWhatsAppFlowsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    def list_whats_app_message_templates(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_message_templates_output.ListWhatsAppMessageTemplatesOutput":
        """<p>Lists WhatsApp message templates for a specific WhatsApp Business Account.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to list templates for.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page (1-100).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.list_whats_app_message_templates_input.ListWhatsAppMessageTemplatesInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_message_templates_output.ListWhatsAppMessageTemplatesOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_message_templates

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_message_templates.list_whats_app_message_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_message_templates_input.ListWhatsAppMessageTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    def list_whats_app_template_library(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
        filters: Optional["aws_sdk_socialmessaging.types.filter.Filter"] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_template_library_output.ListWhatsAppTemplateLibraryOutput":
        """<p>Lists templates available in Meta's template library for WhatsApp messaging.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page (1-100).</p>
            id: <p>The ID of the WhatsApp Business Account to list library templates for.</p>
            filters: <p>Map of filters to apply (searchKey, topic, usecase, industry, language).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.list_whats_app_template_library_input.ListWhatsAppTemplateLibraryInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_template_library_output.ListWhatsAppTemplateLibraryOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_template_library

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_template_library.list_whats_app_template_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_template_library_input.ListWhatsAppTemplateLibraryInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["id"] = id
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def publish_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.publish_whats_app_flow_output.PublishWhatsAppFlowOutput":
        """<p>Publishes a WhatsApp Flow, making it available for use in template messages. The Flow must be in DRAFT status with valid Flow JSON that passes Meta's validation. This is an irreversible operation.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to publish.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.publish_whats_app_flow_input.PublishWhatsAppFlowInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.publish_whats_app_flow_output.PublishWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.publish_whats_app_flow

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.publish_whats_app_flow.publish_whats_app_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.publish_whats_app_flow_input.PublishWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_whats_app_business_account_event_destinations(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        event_destinations: "aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_output.PutWhatsAppBusinessAccountEventDestinationsOutput":
        r"""<p>Add an event destination to log event data from WhatsApp for a WhatsApp Business Account (WABA). A WABA can only have one event destination at a time. All resources associated with the WABA use the same event destination.</p>

        Args:
            id: <p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html\">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
            event_destinations: <p>An array of <code>WhatsAppBusinessAccountEventDestination</code> event destinations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_input.PutWhatsAppBusinessAccountEventDestinationsInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_output.PutWhatsAppBusinessAccountEventDestinationsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.put_whats_app_business_account_event_destinations

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.put_whats_app_business_account_event_destinations.put_whats_app_business_account_event_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_input.PutWhatsAppBusinessAccountEventDestinationsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["event_destinations"] = event_destinations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        flow_name: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_name.MetaFlowName"
        ] = None,
        categories: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.update_whats_app_flow_output.UpdateWhatsAppFlowOutput":
        r"""<p>Updates the metadata of a WhatsApp Flow, such as its name or categories. This does not update the Flow JSON definition. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppFlowAssets.html\">UpdateWhatsAppFlowAssets</a> to update the Flow JSON.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to update.</p>
            flow_name: <p>The updated name for the Flow.</p>
            categories: <p>The updated categories for the Flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.update_whats_app_flow_input.UpdateWhatsAppFlowInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.update_whats_app_flow_output.UpdateWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow.update_whats_app_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.update_whats_app_flow_input.UpdateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
        if flow_name is not None:
            input_["flow_name"] = flow_name
        if categories is not None:
            input_["categories"] = categories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_whats_app_flow_assets(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        flow_json: "aws_sdk_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.update_whats_app_flow_assets_output.UpdateWhatsAppFlowAssetsOutput":
        """<p>Updates the Flow JSON definition (assets) of a WhatsApp Flow. Updating a published Flow's assets reverts it to DRAFT status, requiring re-publishing.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow whose assets to update.</p>
            flow_json: <p>The updated Flow JSON definition. Maximum size is 10 MB.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.update_whats_app_flow_assets_input.UpdateWhatsAppFlowAssetsInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.update_whats_app_flow_assets_output.UpdateWhatsAppFlowAssetsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow_assets

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow_assets.update_whats_app_flow_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.update_whats_app_flow_assets_input.UpdateWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
        input_["flow_json"] = flow_json

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_whats_app_message_template(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        template_name: Optional[
            "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
        ] = None,
        template_language_code: Optional[
            "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
        ] = None,
        parameter_format: Optional[
            "aws_sdk_socialmessaging.types.meta_parameter_format.MetaParameterFormat"
        ] = None,
        template_category: Optional[
            "aws_sdk_socialmessaging.types.meta_template_category.MetaTemplateCategory"
        ] = None,
        template_components: Optional[
            "aws_sdk_socialmessaging.types.meta_template_components.MetaTemplateComponents"
        ] = None,
        cta_url_link_tracking_opted_out: Optional[
            "aws_sdk_socialmessaging.types.meta_template_cta_link_tracking_opted_out.MetaTemplateCtaLinkTrackingOptedOut"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.update_whats_app_message_template_output.UpdateWhatsAppMessageTemplateOutput":
        """<p>Updates an existing WhatsApp message template.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            template_name: <p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            template_language_code: <p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            parameter_format: <p>The format specification for parameters in the template, this can be either 'named' or 'positional'.</p>
            template_category: <p>The new category for the template (for example, UTILITY or MARKETING).</p>
            template_components: <p>The updated components of the template as a JSON blob (maximum 3000 characters).</p>
            cta_url_link_tracking_opted_out: <p>When true, disables click tracking for call-to-action URL buttons in the template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.update_whats_app_message_template_input.UpdateWhatsAppMessageTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.update_whats_app_message_template_output.UpdateWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_message_template

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_message_template.update_whats_app_message_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.update_whats_app_message_template_input.UpdateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if template_name is not None:
            input_["template_name"] = template_name
        if template_language_code is not None:
            input_["template_language_code"] = template_language_code
        if parameter_format is not None:
            input_["parameter_format"] = parameter_format
        if template_category is not None:
            input_["template_category"] = template_category
        if template_components is not None:
            input_["template_components"] = template_components
        if cta_url_link_tracking_opted_out is not None:
            input_["cta_url_link_tracking_opted_out"] = cta_url_link_tracking_opted_out

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLinkedWhatsAppBusinessAccountResource:
    def __init__(self, service: AsyncSocialMessagingClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        signup_callback: Optional[
            "aws_sdk_socialmessaging.types.whats_app_signup_callback.WhatsAppSignupCallback"
        ] = None,
        setup_finalization: Optional[
            "aws_sdk_socialmessaging.types.whats_app_setup_finalization.WhatsAppSetupFinalization"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput":
        """<p>This is only used through the Amazon Web Services console during sign-up to associate your WhatsApp Business Account to your Amazon Web Services account.</p>

        Args:
            signup_callback: <p>Contains the callback access token.</p>
            setup_finalization: <p>A JSON object that contains the phone numbers and WhatsApp Business Account to link to your account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.associate_whats_app_business_account_output.AssociateWhatsAppBusinessAccountOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.associate_whats_app_business_account

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.associate_whats_app_business_account.async_associate_whats_app_business_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.associate_whats_app_business_account_input.AssociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
        if signup_callback is not None:
            input_["signup_callback"] = signup_callback
        if setup_finalization is not None:
            input_["setup_finalization"] = setup_finalization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_output.GetLinkedWhatsAppBusinessAccountOutput":
        r"""<p>Get the details of your linked WhatsApp Business Account.</p>

        Args:
            id: <p>The unique identifier, from Amazon Web Services, of the linked WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html\">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_input.GetLinkedWhatsAppBusinessAccountInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_output.GetLinkedWhatsAppBusinessAccountOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account.async_get_linked_whats_app_business_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_input.GetLinkedWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_output.DisassociateWhatsAppBusinessAccountOutput":
        r"""<p>Disassociate a WhatsApp Business Account (WABA) from your Amazon Web Services account.</p>

        Args:
            id: <p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html\">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_input.DisassociateWhatsAppBusinessAccountInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_output.DisassociateWhatsAppBusinessAccountOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.disassociate_whats_app_business_account

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.disassociate_whats_app_business_account.async_disassociate_whats_app_business_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.disassociate_whats_app_business_account_input.DisassociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_output.ListLinkedWhatsAppBusinessAccountsOutput":
        """<p>List all WhatsApp Business Accounts linked to your Amazon Web Services account.</p>

        Args:
            next_token: <p>The next token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_input.ListLinkedWhatsAppBusinessAccountsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_output.ListLinkedWhatsAppBusinessAccountsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_linked_whats_app_business_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.list_linked_whats_app_business_accounts.async_list_linked_whats_app_business_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_linked_whats_app_business_accounts_input.ListLinkedWhatsAppBusinessAccountsInput = {}  # type: ignore[typeddict-item]
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

    async def create_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_name: "aws_sdk_socialmessaging.types.meta_flow_name.MetaFlowName",
        categories: "aws_sdk_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        flow_json: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob"
        ] = None,
        publish: Optional[bool] = None,
        clone_flow_id: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_flow_output.CreateWhatsAppFlowOutput":
        """<p>Creates a new WhatsApp Flow. Flows enable businesses to create rich, interactive forms and experiences that users can complete without leaving WhatsApp. The Flow is created in DRAFT status. If <code>publish</code> is set to <code>true</code> and a valid <code>flowJson</code> is provided, the Flow is published immediately.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to associate with this Flow.</p>
            flow_name: <p>The name of the Flow. Must be unique within the WhatsApp Business Account.</p>
            categories: <p>The categories that classify the business purpose of the Flow. At least one category is required.</p>
            flow_json: <p>The Flow JSON definition that describes the screens, components, and logic of the Flow. Maximum size is 10 MB.</p>
            publish: <p>Set to <code>true</code> to publish the Flow immediately after creation. Requires a valid <code>flowJson</code> that passes Meta's validation.</p>
            clone_flow_id: <p>The ID of an existing Flow within the same WhatsApp Business Account to clone.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.create_whats_app_flow_input.CreateWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_flow_output.CreateWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_flow

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_flow.async_create_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_flow_input.CreateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_name"] = flow_name
        input_["categories"] = categories
        if flow_json is not None:
            input_["flow_json"] = flow_json
        if publish is not None:
            input_["publish"] = publish
        if clone_flow_id is not None:
            input_["clone_flow_id"] = clone_flow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_whats_app_message_template(
        self,
        template_definition: "aws_sdk_socialmessaging.types.meta_template_definition.MetaTemplateDefinition",
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_message_template_output.CreateWhatsAppMessageTemplateOutput":
        """<p>Creates a new WhatsApp message template from a custom definition.</p> <note> <p>Amazon Web Services End User Messaging Social does not store any WhatsApp message template content.</p> </note>

        Args:
            template_definition: <p>The complete template definition as a JSON blob.</p>
            id: <p>The ID of the WhatsApp Business Account to associate with this template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.create_whats_app_message_template_input.CreateWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_message_template_output.CreateWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template.async_create_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_message_template_input.CreateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_definition"] = template_definition
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_whats_app_message_template_from_library(
        self,
        meta_library_template: "aws_sdk_socialmessaging.types.meta_library_template.MetaLibraryTemplate",
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_output.CreateWhatsAppMessageTemplateFromLibraryOutput":
        """<p>Creates a new WhatsApp message template using a template from Meta's template library.</p>

        Args:
            meta_library_template: <p>The template configuration from Meta's library, including customizations for buttons and body text.</p>
            id: <p>The ID of the WhatsApp Business Account to associate with this template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_input.CreateWhatsAppMessageTemplateFromLibraryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_output.CreateWhatsAppMessageTemplateFromLibraryOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_from_library

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_from_library.async_create_whats_app_message_template_from_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_message_template_from_library_input.CreateWhatsAppMessageTemplateFromLibraryInput = {}  # type: ignore[typeddict-item]
        input_["meta_library_template"] = meta_library_template
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_whats_app_message_template_media(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        source_s3_file: Optional["aws_sdk_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "aws_sdk_socialmessaging.types.create_whats_app_message_template_media_output.CreateWhatsAppMessageTemplateMediaOutput":
        """<p>Uploads media for use in a WhatsApp message template.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this media upload.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.create_whats_app_message_template_media_input.CreateWhatsAppMessageTemplateMediaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.create_whats_app_message_template_media_output.CreateWhatsAppMessageTemplateMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_media

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.create_whats_app_message_template_media.async_create_whats_app_message_template_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.create_whats_app_message_template_media_input.CreateWhatsAppMessageTemplateMediaInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.delete_whats_app_flow_output.DeleteWhatsAppFlowOutput":
        """<p>Deletes a WhatsApp Flow permanently. Only Flows in DRAFT status can be deleted. Published or deprecated Flows cannot be deleted.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.delete_whats_app_flow_input.DeleteWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.delete_whats_app_flow_output.DeleteWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_flow

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_flow.async_delete_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.delete_whats_app_flow_input.DeleteWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_whats_app_message_template(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        template_name: "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        delete_all_languages: Optional[
            "aws_sdk_socialmessaging.types.delete_all_languages.DeleteAllLanguages"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.delete_whats_app_message_template_output.DeleteWhatsAppMessageTemplateOutput":
        """<p>Deletes a WhatsApp message template.</p>

        Args:
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            delete_all_languages: <p>If true, deletes all language versions of the template.</p>
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            template_name: <p>The name of the template to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.delete_whats_app_message_template_input.DeleteWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.delete_whats_app_message_template_output.DeleteWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_template

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_template.async_delete_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.delete_whats_app_message_template_input.DeleteWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if delete_all_languages is not None:
            input_["delete_all_languages"] = delete_all_languages
        input_["id"] = id
        input_["template_name"] = template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deprecate_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.deprecate_whats_app_flow_output.DeprecateWhatsAppFlowOutput":
        """<p>Deprecates a published WhatsApp Flow, marking it as no longer recommended for use. The Flow must be in PUBLISHED status. This is an irreversible operation.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to deprecate.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.deprecate_whats_app_flow_input.DeprecateWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.deprecate_whats_app_flow_output.DeprecateWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.deprecate_whats_app_flow

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.deprecate_whats_app_flow.async_deprecate_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.deprecate_whats_app_flow_input.DeprecateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> (
        "aws_sdk_socialmessaging.types.get_whats_app_flow_output.GetWhatsAppFlowOutput"
    ):
        """<p>Retrieves the metadata and status of a WhatsApp Flow, including validation errors, preview information, and health status.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.get_whats_app_flow_input.GetWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_flow_output.GetWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow.async_get_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_flow_input.GetWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_whats_app_flow_preview(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        invalidate: Optional[bool] = None,
    ) -> "aws_sdk_socialmessaging.types.get_whats_app_flow_preview_output.GetWhatsAppFlowPreviewOutput":
        """<p>Generates a web preview URL for testing a WhatsApp Flow before publishing. Preview URLs expire in 30 days and can be shared with stakeholders for review.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to preview.</p>
            invalidate: <p>Set to <code>true</code> to force generation of a new preview URL. Use this if the previous URL has been compromised or you want a fresh expiration period.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.get_whats_app_flow_preview_input.GetWhatsAppFlowPreviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_flow_preview_output.GetWhatsAppFlowPreviewOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow_preview

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_flow_preview.async_get_whats_app_flow_preview(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_flow_preview_input.GetWhatsAppFlowPreviewInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
        if invalidate is not None:
            input_["invalidate"] = invalidate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_whats_app_message_template(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        template_name: Optional[
            "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
        ] = None,
        template_language_code: Optional[
            "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.get_whats_app_message_template_output.GetWhatsAppMessageTemplateOutput":
        """<p>Retrieves a specific WhatsApp message template.</p>

        Args:
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            template_name: <p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            template_language_code: <p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.get_whats_app_message_template_input.GetWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_message_template_output.GetWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_template

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_template.async_get_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_message_template_input.GetWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        input_["id"] = id
        if template_name is not None:
            input_["template_name"] = template_name
        if template_language_code is not None:
            input_["template_language_code"] = template_language_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_whats_app_flow_assets(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_flow_assets_output.ListWhatsAppFlowAssetsOutput":
        """<p>Lists the assets (Flow JSON definition) of a WhatsApp Flow with presigned download URLs. Download URLs are generated by Meta and expire after a short period.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow whose assets to list.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.list_whats_app_flow_assets_input.ListWhatsAppFlowAssetsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_flow_assets_output.ListWhatsAppFlowAssetsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flow_assets

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flow_assets.async_list_whats_app_flow_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_flow_assets_input.ListWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
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

    async def list_whats_app_flows(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_flows_output.ListWhatsAppFlowsOutput":
        """<p>Lists all WhatsApp Flows for a WhatsApp Business Account. Returns summary information including Flow ID, name, status, and categories.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to list Flows for.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.list_whats_app_flows_input.ListWhatsAppFlowsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_flows_output.ListWhatsAppFlowsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flows

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_flows.async_list_whats_app_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_flows_input.ListWhatsAppFlowsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    async def list_whats_app_message_templates(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_message_templates_output.ListWhatsAppMessageTemplatesOutput":
        """<p>Lists WhatsApp message templates for a specific WhatsApp Business Account.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account to list templates for.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page (1-100).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.list_whats_app_message_templates_input.ListWhatsAppMessageTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_message_templates_output.ListWhatsAppMessageTemplatesOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_message_templates

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_message_templates.async_list_whats_app_message_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_message_templates_input.ListWhatsAppMessageTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    async def list_whats_app_template_library(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_socialmessaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_socialmessaging.types.max_results.MaxResults"
        ] = None,
        filters: Optional["aws_sdk_socialmessaging.types.filter.Filter"] = None,
    ) -> "aws_sdk_socialmessaging.types.list_whats_app_template_library_output.ListWhatsAppTemplateLibraryOutput":
        """<p>Lists templates available in Meta's template library for WhatsApp messaging.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return per page (1-100).</p>
            id: <p>The ID of the WhatsApp Business Account to list library templates for.</p>
            filters: <p>Map of filters to apply (searchKey, topic, usecase, industry, language).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.list_whats_app_template_library_input.ListWhatsAppTemplateLibraryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.list_whats_app_template_library_output.ListWhatsAppTemplateLibraryOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_template_library

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.list_whats_app_template_library.async_list_whats_app_template_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_whats_app_template_library_input.ListWhatsAppTemplateLibraryInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["id"] = id
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def publish_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.publish_whats_app_flow_output.PublishWhatsAppFlowOutput":
        """<p>Publishes a WhatsApp Flow, making it available for use in template messages. The Flow must be in DRAFT status with valid Flow JSON that passes Meta's validation. This is an irreversible operation.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to publish.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.publish_whats_app_flow_input.PublishWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.publish_whats_app_flow_output.PublishWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.publish_whats_app_flow

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.publish_whats_app_flow.async_publish_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.publish_whats_app_flow_input.PublishWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_whats_app_business_account_event_destinations(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        event_destinations: "aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_output.PutWhatsAppBusinessAccountEventDestinationsOutput":
        r"""<p>Add an event destination to log event data from WhatsApp for a WhatsApp Business Account (WABA). A WABA can only have one event destination at a time. All resources associated with the WABA use the same event destination.</p>

        Args:
            id: <p>The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as <code>waba-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html\">ListLinkedWhatsAppBusinessAccounts</a> to list all WABAs and their details.</p>
            event_destinations: <p>An array of <code>WhatsAppBusinessAccountEventDestination</code> event destinations.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_input.PutWhatsAppBusinessAccountEventDestinationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_output.PutWhatsAppBusinessAccountEventDestinationsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.put_whats_app_business_account_event_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.put_whats_app_business_account_event_destinations.async_put_whats_app_business_account_event_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.put_whats_app_business_account_event_destinations_input.PutWhatsAppBusinessAccountEventDestinationsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["event_destinations"] = event_destinations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_whats_app_flow(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        flow_name: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_name.MetaFlowName"
        ] = None,
        categories: Optional[
            "aws_sdk_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.update_whats_app_flow_output.UpdateWhatsAppFlowOutput":
        r"""<p>Updates the metadata of a WhatsApp Flow, such as its name or categories. This does not update the Flow JSON definition. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppFlowAssets.html\">UpdateWhatsAppFlowAssets</a> to update the Flow JSON.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow to update.</p>
            flow_name: <p>The updated name for the Flow.</p>
            categories: <p>The updated categories for the Flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.update_whats_app_flow_input.UpdateWhatsAppFlowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.update_whats_app_flow_output.UpdateWhatsAppFlowOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow.async_update_whats_app_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.update_whats_app_flow_input.UpdateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
        if flow_name is not None:
            input_["flow_name"] = flow_name
        if categories is not None:
            input_["categories"] = categories

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_whats_app_flow_assets(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId",
        flow_json: "aws_sdk_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.update_whats_app_flow_assets_output.UpdateWhatsAppFlowAssetsOutput":
        """<p>Updates the Flow JSON definition (assets) of a WhatsApp Flow. Updating a published Flow's assets reverts it to DRAFT status, requiring re-publishing.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this Flow.</p>
            flow_id: <p>The unique identifier of the Flow whose assets to update.</p>
            flow_json: <p>The updated Flow JSON definition. Maximum size is 10 MB.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.update_whats_app_flow_assets_input.UpdateWhatsAppFlowAssetsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.update_whats_app_flow_assets_output.UpdateWhatsAppFlowAssetsOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow_assets

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_flow_assets.async_update_whats_app_flow_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.update_whats_app_flow_assets_input.UpdateWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["flow_id"] = flow_id
        input_["flow_json"] = flow_json

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_whats_app_message_template(
        self,
        id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        meta_template_id: Optional[
            "aws_sdk_socialmessaging.types.meta_template_id.MetaTemplateId"
        ] = None,
        template_name: Optional[
            "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
        ] = None,
        template_language_code: Optional[
            "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
        ] = None,
        parameter_format: Optional[
            "aws_sdk_socialmessaging.types.meta_parameter_format.MetaParameterFormat"
        ] = None,
        template_category: Optional[
            "aws_sdk_socialmessaging.types.meta_template_category.MetaTemplateCategory"
        ] = None,
        template_components: Optional[
            "aws_sdk_socialmessaging.types.meta_template_components.MetaTemplateComponents"
        ] = None,
        cta_url_link_tracking_opted_out: Optional[
            "aws_sdk_socialmessaging.types.meta_template_cta_link_tracking_opted_out.MetaTemplateCtaLinkTrackingOptedOut"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.update_whats_app_message_template_output.UpdateWhatsAppMessageTemplateOutput":
        """<p>Updates an existing WhatsApp message template.</p>

        Args:
            id: <p>The ID of the WhatsApp Business Account associated with this template.</p>
            meta_template_id: <p>The numeric ID of the template assigned by Meta.</p>
            template_name: <p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            template_language_code: <p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>
            parameter_format: <p>The format specification for parameters in the template, this can be either 'named' or 'positional'.</p>
            template_category: <p>The new category for the template (for example, UTILITY or MARKETING).</p>
            template_components: <p>The updated components of the template as a JSON blob (maximum 3000 characters).</p>
            cta_url_link_tracking_opted_out: <p>When true, disables click tracking for call-to-action URL buttons in the template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.update_whats_app_message_template_input.UpdateWhatsAppMessageTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.update_whats_app_message_template_output.UpdateWhatsAppMessageTemplateOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_message_template

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.update_whats_app_message_template.async_update_whats_app_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.update_whats_app_message_template_input.UpdateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if meta_template_id is not None:
            input_["meta_template_id"] = meta_template_id
        if template_name is not None:
            input_["template_name"] = template_name
        if template_language_code is not None:
            input_["template_language_code"] = template_language_code
        if parameter_format is not None:
            input_["parameter_format"] = parameter_format
        if template_category is not None:
            input_["template_category"] = template_category
        if template_components is not None:
            input_["template_components"] = template_components
        if cta_url_link_tracking_opted_out is not None:
            input_["cta_url_link_tracking_opted_out"] = cta_url_link_tracking_opted_out

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
