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
    import aws_sdk_socialmessaging.types.delete_whats_app_message_media_input
    import aws_sdk_socialmessaging.types.delete_whats_app_message_media_output
    import aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input
    import aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output
    import aws_sdk_socialmessaging.types.get_whats_app_message_media_input
    import aws_sdk_socialmessaging.types.get_whats_app_message_media_output
    import aws_sdk_socialmessaging.types.post_whats_app_message_media_input
    import aws_sdk_socialmessaging.types.post_whats_app_message_media_output
    import aws_sdk_socialmessaging.types.s3_file
    import aws_sdk_socialmessaging.types.s3_presigned_url
    import aws_sdk_socialmessaging.types.send_whats_app_message_input
    import aws_sdk_socialmessaging.types.send_whats_app_message_output
    import aws_sdk_socialmessaging.types.whats_app_media_id
    import aws_sdk_socialmessaging.types.whats_app_message_blob
    import aws_sdk_socialmessaging.types.whats_app_phone_number_id
    from aws_sdk_socialmessaging._services.async_social_messaging import (
        AsyncSocialMessagingClient,
        AsyncSocialMessagingClientConfig,
    )
    from aws_sdk_socialmessaging._services.social_messaging import (
        SocialMessagingClient,
        SocialMessagingClientConfig,
    )


class LinkedWhatsAppPhoneNumberResource:
    def __init__(self, service: SocialMessagingClient) -> None:
        self._service = service

    def read(
        self,
        id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput":
        r"""<p>Retrieve the WABA account id and phone number details of a WhatsApp business account phone number.</p>

        Args:
            id: <p>The unique identifier of the phone number. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number.get_linked_whats_app_business_account_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_whats_app_message_media(
        self,
        media_id: "aws_sdk_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput":
        r"""<p>Delete a media object from the WhatsApp service. If the object is still in an Amazon S3 bucket you should delete it from there too.</p>

        Args:
            media_id: <p>The unique identifier of the media file to delete. Use the <code>mediaId</code> returned from <a href=\"https://console.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html\">PostWhatsAppMessageMedia</a>.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_media

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_media.delete_whats_app_message_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
        input_["media_id"] = media_id
        input_["origination_phone_number_id"] = origination_phone_number_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_whats_app_message_media(
        self,
        media_id: "aws_sdk_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        metadata_only: Optional[bool] = None,
        destination_s3_presigned_url: Optional[
            "aws_sdk_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        destination_s3_file: Optional[
            "aws_sdk_socialmessaging.types.s3_file.S3File"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput":
        r"""<p>Get a media file from the WhatsApp service. On successful completion the media file is retrieved from Meta and stored in the specified Amazon S3 bucket. Use either <code>destinationS3File</code> or <code>destinationS3PresignedUrl</code> for the destination. If both are used then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            media_id: <p>The unique identifier for the media file.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            metadata_only: <p>Set to <code>True</code> to get only the metadata for the file.</p>
            destination_s3_presigned_url: <p>The presign url of the media file.</p>
            destination_s3_file: <p>The <code>bucketName</code> and <code>key</code> of the S3 media file.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_media

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_media.get_whats_app_message_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
        input_["media_id"] = media_id
        input_["origination_phone_number_id"] = origination_phone_number_id
        if metadata_only is not None:
            input_["metadata_only"] = metadata_only
        if destination_s3_presigned_url is not None:
            input_["destination_s3_presigned_url"] = destination_s3_presigned_url
        if destination_s3_file is not None:
            input_["destination_s3_file"] = destination_s3_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def post_whats_app_message_media(
        self,
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
        source_s3_presigned_url: Optional[
            "aws_sdk_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        source_s3_file: Optional["aws_sdk_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "aws_sdk_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput":
        r"""<p>Upload a media file to the WhatsApp service. Only the specified <code>originationPhoneNumberId</code> has the permissions to send the media file when using <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html\">SendWhatsAppMessage</a>. You must use either <code>sourceS3File</code> or <code>sourceS3PresignedUrl</code> for the source. If both or neither are specified then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number to associate with the WhatsApp media file. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            source_s3_presigned_url: <p>The source presign url of the media file.</p>
            source_s3_file: <p>The source S3 url for the media file.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.post_whats_app_message_media

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.post_whats_app_message_media.post_whats_app_message_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
        input_["origination_phone_number_id"] = origination_phone_number_id
        if source_s3_presigned_url is not None:
            input_["source_s3_presigned_url"] = source_s3_presigned_url
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_whats_app_message(
        self,
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        message: "aws_sdk_socialmessaging.types.whats_app_message_blob.WhatsAppMessageBlob",
        meta_api_version: str,
        *,
        config_overrides: Optional[SocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput":
        r"""<p>Send a WhatsApp message. For examples of sending a message using the Amazon Web Services CLI, see <a href=\"https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message.html\">Sending messages</a> in the <i> <i>Amazon Web Services End User Messaging Social User Guide</i> </i>.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number used to send the WhatsApp message. If you are sending a media file only the <code>originationPhoneNumberId</code> used to upload the file can be used. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            message: <p>The message to send through WhatsApp. The length is in KB. The message field passes through a WhatsApp Message object, see <a href=\"https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages\">Messages</a> in the <i>WhatsApp Business Platform Cloud API Reference</i>.</p>
            meta_api_version: <p>The API version for the request formatted as <code>v{VersionNumber}</code>. For a list of supported API versions and Amazon Web Services Regions, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html\"> <i>Amazon Web Services End User Messaging Social API</i> Service Endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput]",
        ) -> OperationResponse[
            "aws_sdk_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.send_whats_app_message

            output, http_response = (
                aws_sdk_socialmessaging._operations.social_messaging.send_whats_app_message.send_whats_app_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput = {}  # type: ignore[typeddict-item]
        input_["origination_phone_number_id"] = origination_phone_number_id
        input_["message"] = message
        input_["meta_api_version"] = meta_api_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLinkedWhatsAppPhoneNumberResource:
    def __init__(self, service: AsyncSocialMessagingClient) -> None:
        self._service = service

    async def read(
        self,
        id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput":
        r"""<p>Retrieve the WABA account id and phone number details of a WhatsApp business account phone number.</p>

        Args:
            id: <p>The unique identifier of the phone number. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_output.GetLinkedWhatsAppBusinessAccountPhoneNumberOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.get_linked_whats_app_business_account_phone_number.async_get_linked_whats_app_business_account_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_linked_whats_app_business_account_phone_number_input.GetLinkedWhatsAppBusinessAccountPhoneNumberInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_whats_app_message_media(
        self,
        media_id: "aws_sdk_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput":
        r"""<p>Delete a media object from the WhatsApp service. If the object is still in an Amazon S3 bucket you should delete it from there too.</p>

        Args:
            media_id: <p>The unique identifier of the media file to delete. Use the <code>mediaId</code> returned from <a href=\"https://console.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html\">PostWhatsAppMessageMedia</a>.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.delete_whats_app_message_media_output.DeleteWhatsAppMessageMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_media

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.delete_whats_app_message_media.async_delete_whats_app_message_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.delete_whats_app_message_media_input.DeleteWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
        input_["media_id"] = media_id
        input_["origination_phone_number_id"] = origination_phone_number_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_whats_app_message_media(
        self,
        media_id: "aws_sdk_socialmessaging.types.whats_app_media_id.WhatsAppMediaId",
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        metadata_only: Optional[bool] = None,
        destination_s3_presigned_url: Optional[
            "aws_sdk_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        destination_s3_file: Optional[
            "aws_sdk_socialmessaging.types.s3_file.S3File"
        ] = None,
    ) -> "aws_sdk_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput":
        r"""<p>Get a media file from the WhatsApp service. On successful completion the media file is retrieved from Meta and stored in the specified Amazon S3 bucket. Use either <code>destinationS3File</code> or <code>destinationS3PresignedUrl</code> for the destination. If both are used then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            media_id: <p>The unique identifier for the media file.</p>
            origination_phone_number_id: <p>The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            metadata_only: <p>Set to <code>True</code> to get only the metadata for the file.</p>
            destination_s3_presigned_url: <p>The presign url of the media file.</p>
            destination_s3_file: <p>The <code>bucketName</code> and <code>key</code> of the S3 media file.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.get_whats_app_message_media_output.GetWhatsAppMessageMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_media

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.get_whats_app_message_media.async_get_whats_app_message_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.get_whats_app_message_media_input.GetWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
        input_["media_id"] = media_id
        input_["origination_phone_number_id"] = origination_phone_number_id
        if metadata_only is not None:
            input_["metadata_only"] = metadata_only
        if destination_s3_presigned_url is not None:
            input_["destination_s3_presigned_url"] = destination_s3_presigned_url
        if destination_s3_file is not None:
            input_["destination_s3_file"] = destination_s3_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def post_whats_app_message_media(
        self,
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
        source_s3_presigned_url: Optional[
            "aws_sdk_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
        ] = None,
        source_s3_file: Optional["aws_sdk_socialmessaging.types.s3_file.S3File"] = None,
    ) -> "aws_sdk_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput":
        r"""<p>Upload a media file to the WhatsApp service. Only the specified <code>originationPhoneNumberId</code> has the permissions to send the media file when using <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html\">SendWhatsAppMessage</a>. You must use either <code>sourceS3File</code> or <code>sourceS3PresignedUrl</code> for the source. If both or neither are specified then an <code>InvalidParameterException</code> is returned.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number to associate with the WhatsApp media file. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            source_s3_presigned_url: <p>The source presign url of the media file.</p>
            source_s3_file: <p>The source S3 url for the media file.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.post_whats_app_message_media_output.PostWhatsAppMessageMediaOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.post_whats_app_message_media

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.post_whats_app_message_media.async_post_whats_app_message_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.post_whats_app_message_media_input.PostWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
        input_["origination_phone_number_id"] = origination_phone_number_id
        if source_s3_presigned_url is not None:
            input_["source_s3_presigned_url"] = source_s3_presigned_url
        if source_s3_file is not None:
            input_["source_s3_file"] = source_s3_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_whats_app_message(
        self,
        origination_phone_number_id: "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId",
        message: "aws_sdk_socialmessaging.types.whats_app_message_blob.WhatsAppMessageBlob",
        meta_api_version: str,
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput":
        r"""<p>Send a WhatsApp message. For examples of sending a message using the Amazon Web Services CLI, see <a href=\"https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message.html\">Sending messages</a> in the <i> <i>Amazon Web Services End User Messaging Social User Guide</i> </i>.</p>

        Args:
            origination_phone_number_id: <p>The ID of the phone number used to send the WhatsApp message. If you are sending a media file only the <code>originationPhoneNumberId</code> used to upload the file can be used. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>
            message: <p>The message to send through WhatsApp. The length is in KB. The message field passes through a WhatsApp Message object, see <a href=\"https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages\">Messages</a> in the <i>WhatsApp Business Platform Cloud API Reference</i>.</p>
            meta_api_version: <p>The API version for the request formatted as <code>v{VersionNumber}</code>. For a list of supported API versions and Amazon Web Services Regions, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html\"> <i>Amazon Web Services End User Messaging Social API</i> Service Endpoints</a> in the <i>Amazon Web Services General Reference</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.send_whats_app_message_output.SendWhatsAppMessageOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.send_whats_app_message

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.send_whats_app_message.async_send_whats_app_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.send_whats_app_message_input.SendWhatsAppMessageInput = {}  # type: ignore[typeddict-item]
        input_["origination_phone_number_id"] = origination_phone_number_id
        input_["message"] = message
        input_["meta_api_version"] = meta_api_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
