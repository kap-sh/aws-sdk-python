"""Generated from Smithy shape ``com.amazonaws.chime#UCBuzzConsoleService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_chime._auth._signers
import aws_sdk_chime._auth._sigv4
from aws_sdk_chime._auth._identity import Credentials
from aws_sdk_chime._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_chime._auth._zapros_handler import AuthMiddleware
from aws_sdk_chime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_chime.types.account_name
    import aws_sdk_chime.types.account_settings
    import aws_sdk_chime.types.alexa_for_business_metadata
    import aws_sdk_chime.types.alpha2_country_code
    import aws_sdk_chime.types.associate_phone_number_with_user_request
    import aws_sdk_chime.types.associate_phone_number_with_user_response
    import aws_sdk_chime.types.associate_signin_delegate_groups_with_account_request
    import aws_sdk_chime.types.associate_signin_delegate_groups_with_account_response
    import aws_sdk_chime.types.batch_create_room_membership_request
    import aws_sdk_chime.types.batch_create_room_membership_response
    import aws_sdk_chime.types.batch_delete_phone_number_request
    import aws_sdk_chime.types.batch_delete_phone_number_response
    import aws_sdk_chime.types.batch_suspend_user_request
    import aws_sdk_chime.types.batch_suspend_user_response
    import aws_sdk_chime.types.batch_unsuspend_user_request
    import aws_sdk_chime.types.batch_unsuspend_user_response
    import aws_sdk_chime.types.batch_update_phone_number_request
    import aws_sdk_chime.types.batch_update_phone_number_response
    import aws_sdk_chime.types.batch_update_user_request
    import aws_sdk_chime.types.batch_update_user_response
    import aws_sdk_chime.types.business_calling_settings
    import aws_sdk_chime.types.calling_name
    import aws_sdk_chime.types.client_request_token
    import aws_sdk_chime.types.create_account_request
    import aws_sdk_chime.types.create_account_response
    import aws_sdk_chime.types.create_bot_request
    import aws_sdk_chime.types.create_bot_response
    import aws_sdk_chime.types.create_meeting_dial_out_request
    import aws_sdk_chime.types.create_meeting_dial_out_response
    import aws_sdk_chime.types.create_phone_number_order_request
    import aws_sdk_chime.types.create_phone_number_order_response
    import aws_sdk_chime.types.create_room_membership_request
    import aws_sdk_chime.types.create_room_membership_response
    import aws_sdk_chime.types.create_room_request
    import aws_sdk_chime.types.create_room_response
    import aws_sdk_chime.types.create_user_request
    import aws_sdk_chime.types.create_user_response
    import aws_sdk_chime.types.delete_account_request
    import aws_sdk_chime.types.delete_account_response
    import aws_sdk_chime.types.delete_events_configuration_request
    import aws_sdk_chime.types.delete_phone_number_request
    import aws_sdk_chime.types.delete_room_membership_request
    import aws_sdk_chime.types.delete_room_request
    import aws_sdk_chime.types.disassociate_phone_number_from_user_request
    import aws_sdk_chime.types.disassociate_phone_number_from_user_response
    import aws_sdk_chime.types.disassociate_signin_delegate_groups_from_account_request
    import aws_sdk_chime.types.disassociate_signin_delegate_groups_from_account_response
    import aws_sdk_chime.types.e164_phone_number
    import aws_sdk_chime.types.e164_phone_number_list
    import aws_sdk_chime.types.email_address
    import aws_sdk_chime.types.get_account_request
    import aws_sdk_chime.types.get_account_response
    import aws_sdk_chime.types.get_account_settings_request
    import aws_sdk_chime.types.get_account_settings_response
    import aws_sdk_chime.types.get_bot_request
    import aws_sdk_chime.types.get_bot_response
    import aws_sdk_chime.types.get_events_configuration_request
    import aws_sdk_chime.types.get_events_configuration_response
    import aws_sdk_chime.types.get_global_settings_response
    import aws_sdk_chime.types.get_phone_number_order_request
    import aws_sdk_chime.types.get_phone_number_order_response
    import aws_sdk_chime.types.get_phone_number_request
    import aws_sdk_chime.types.get_phone_number_response
    import aws_sdk_chime.types.get_phone_number_settings_response
    import aws_sdk_chime.types.get_retention_settings_request
    import aws_sdk_chime.types.get_retention_settings_response
    import aws_sdk_chime.types.get_room_request
    import aws_sdk_chime.types.get_room_response
    import aws_sdk_chime.types.get_user_request
    import aws_sdk_chime.types.get_user_response
    import aws_sdk_chime.types.get_user_settings_request
    import aws_sdk_chime.types.get_user_settings_response
    import aws_sdk_chime.types.guid_string
    import aws_sdk_chime.types.invite_users_request
    import aws_sdk_chime.types.invite_users_response
    import aws_sdk_chime.types.join_token_string
    import aws_sdk_chime.types.license
    import aws_sdk_chime.types.list_accounts_request
    import aws_sdk_chime.types.list_accounts_response
    import aws_sdk_chime.types.list_bots_request
    import aws_sdk_chime.types.list_bots_response
    import aws_sdk_chime.types.list_phone_number_orders_request
    import aws_sdk_chime.types.list_phone_number_orders_response
    import aws_sdk_chime.types.list_phone_numbers_request
    import aws_sdk_chime.types.list_phone_numbers_response
    import aws_sdk_chime.types.list_room_memberships_request
    import aws_sdk_chime.types.list_room_memberships_response
    import aws_sdk_chime.types.list_rooms_request
    import aws_sdk_chime.types.list_rooms_response
    import aws_sdk_chime.types.list_supported_phone_number_countries_request
    import aws_sdk_chime.types.list_supported_phone_number_countries_response
    import aws_sdk_chime.types.list_users_request
    import aws_sdk_chime.types.list_users_response
    import aws_sdk_chime.types.logout_user_request
    import aws_sdk_chime.types.logout_user_response
    import aws_sdk_chime.types.membership_item_list
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.non_empty_string_list
    import aws_sdk_chime.types.nullable_boolean
    import aws_sdk_chime.types.phone_number_association_name
    import aws_sdk_chime.types.phone_number_max_results
    import aws_sdk_chime.types.phone_number_product_type
    import aws_sdk_chime.types.phone_number_status
    import aws_sdk_chime.types.phone_number_type
    import aws_sdk_chime.types.profile_service_max_results
    import aws_sdk_chime.types.put_events_configuration_request
    import aws_sdk_chime.types.put_events_configuration_response
    import aws_sdk_chime.types.put_retention_settings_request
    import aws_sdk_chime.types.put_retention_settings_response
    import aws_sdk_chime.types.redact_conversation_message_request
    import aws_sdk_chime.types.redact_conversation_message_response
    import aws_sdk_chime.types.redact_room_message_request
    import aws_sdk_chime.types.redact_room_message_response
    import aws_sdk_chime.types.regenerate_security_token_request
    import aws_sdk_chime.types.regenerate_security_token_response
    import aws_sdk_chime.types.reset_personal_pin_request
    import aws_sdk_chime.types.reset_personal_pin_response
    import aws_sdk_chime.types.restore_phone_number_request
    import aws_sdk_chime.types.restore_phone_number_response
    import aws_sdk_chime.types.result_max
    import aws_sdk_chime.types.retention_settings
    import aws_sdk_chime.types.room_membership_role
    import aws_sdk_chime.types.search_available_phone_numbers_request
    import aws_sdk_chime.types.search_available_phone_numbers_response
    import aws_sdk_chime.types.sensitive_string
    import aws_sdk_chime.types.signin_delegate_group_list
    import aws_sdk_chime.types.string
    import aws_sdk_chime.types.toll_free_prefix
    import aws_sdk_chime.types.update_account_request
    import aws_sdk_chime.types.update_account_response
    import aws_sdk_chime.types.update_account_settings_request
    import aws_sdk_chime.types.update_account_settings_response
    import aws_sdk_chime.types.update_bot_request
    import aws_sdk_chime.types.update_bot_response
    import aws_sdk_chime.types.update_global_settings_request
    import aws_sdk_chime.types.update_phone_number_request
    import aws_sdk_chime.types.update_phone_number_request_item_list
    import aws_sdk_chime.types.update_phone_number_response
    import aws_sdk_chime.types.update_phone_number_settings_request
    import aws_sdk_chime.types.update_room_membership_request
    import aws_sdk_chime.types.update_room_membership_response
    import aws_sdk_chime.types.update_room_request
    import aws_sdk_chime.types.update_room_response
    import aws_sdk_chime.types.update_user_request
    import aws_sdk_chime.types.update_user_request_item_list
    import aws_sdk_chime.types.update_user_response
    import aws_sdk_chime.types.update_user_settings_request
    import aws_sdk_chime.types.user_email_list
    import aws_sdk_chime.types.user_id_list
    import aws_sdk_chime.types.user_settings
    import aws_sdk_chime.types.user_type
    import aws_sdk_chime.types.voice_connector_settings


class ChimeClientConfig(TypedDict, total=False):
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


class ChimeClient:
    """A client for the ``Chime`` service.

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
        self.config = ChimeClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[ChimeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ChimeClientConfig = config_overrides or {}
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

    def associate_phone_number_with_user(
        self,
        account_id: "aws_sdk_chime.types.string.String",
        user_id: "aws_sdk_chime.types.string.String",
        e164_phone_number: "aws_sdk_chime.types.e164_phone_number.E164PhoneNumber",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.associate_phone_number_with_user_response.AssociatePhoneNumberWithUserResponse":
        """<p>Associates a phone number with the specified Amazon Chime user.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
            e164_phone_number: <p>The phone number, in E.164 format.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.associate_phone_number_with_user_request.AssociatePhoneNumberWithUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.associate_phone_number_with_user_response.AssociatePhoneNumberWithUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.associate_phone_number_with_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.associate_phone_number_with_user.associate_phone_number_with_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.associate_phone_number_with_user_request.AssociatePhoneNumberWithUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id
        input_["e164_phone_number"] = e164_phone_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_signin_delegate_groups_with_account(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        signin_delegate_groups: "aws_sdk_chime.types.signin_delegate_group_list.SigninDelegateGroupList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.associate_signin_delegate_groups_with_account_response.AssociateSigninDelegateGroupsWithAccountResponse":
        """<p>Associates the specified sign-in delegate groups with the specified Amazon Chime account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            signin_delegate_groups: <p>The sign-in delegate groups.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.associate_signin_delegate_groups_with_account_request.AssociateSigninDelegateGroupsWithAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.associate_signin_delegate_groups_with_account_response.AssociateSigninDelegateGroupsWithAccountResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.associate_signin_delegate_groups_with_account

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.associate_signin_delegate_groups_with_account.associate_signin_delegate_groups_with_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.associate_signin_delegate_groups_with_account_request.AssociateSigninDelegateGroupsWithAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["signin_delegate_groups"] = signin_delegate_groups

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_create_room_membership(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        membership_item_list: "aws_sdk_chime.types.membership_item_list.MembershipItemList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.batch_create_room_membership_response.BatchCreateRoomMembershipResponse":
        """<p>Adds up to 50 members to a chat room in an Amazon Chime Enterprise account. Members can be users or bots. The member role designates whether the member is a chat room administrator or a general chat room member.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            membership_item_list: <p>The list of membership items.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.batch_create_room_membership_request.BatchCreateRoomMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.batch_create_room_membership_response.BatchCreateRoomMembershipResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.batch_create_room_membership

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.batch_create_room_membership.batch_create_room_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.batch_create_room_membership_request.BatchCreateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
        input_["membership_item_list"] = membership_item_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_delete_phone_number(
        self,
        phone_number_ids: "aws_sdk_chime.types.non_empty_string_list.NonEmptyStringList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.batch_delete_phone_number_response.BatchDeletePhoneNumberResponse":
        """<p> Moves phone numbers into the <b>Deletion queue</b>. Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted. </p> <p> Phone numbers remain in the <b>Deletion queue</b> for 7 days before they are deleted permanently. </p>

        Args:
            phone_number_ids: <p>List of phone number IDs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.batch_delete_phone_number_request.BatchDeletePhoneNumberRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.batch_delete_phone_number_response.BatchDeletePhoneNumberResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.batch_delete_phone_number

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.batch_delete_phone_number.batch_delete_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.batch_delete_phone_number_request.BatchDeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
        input_["phone_number_ids"] = phone_number_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_suspend_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_id_list: "aws_sdk_chime.types.user_id_list.UserIdList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.batch_suspend_user_response.BatchSuspendUserResponse":
        """<p>Suspends up to 50 users from a <code>Team</code> or <code>EnterpriseLWA</code> Amazon Chime account. For more information about different account types, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\">Managing Your Amazon Chime Accounts</a> in the <i>Amazon Chime Administration Guide</i>.</p> <p>Users suspended from a <code>Team</code> account are disassociated from the account,but they can continue to use Amazon Chime as free users. To remove the suspension from suspended <code>Team</code> account users, invite them to the <code>Team</code> account again. You can use the <a>InviteUsers</a> action to do so.</p> <p>Users suspended from an <code>EnterpriseLWA</code> account are immediately signed out of Amazon Chime and can no longer sign in. To remove the suspension from suspended <code>EnterpriseLWA</code> account users, use the <a>BatchUnsuspendUser</a> action.</p> <p> To sign out users without suspending them, use the <a>LogoutUser</a> action.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id_list: <p>The request containing the user IDs to suspend.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.batch_suspend_user_request.BatchSuspendUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.batch_suspend_user_response.BatchSuspendUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.batch_suspend_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.batch_suspend_user.batch_suspend_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.batch_suspend_user_request.BatchSuspendUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id_list"] = user_id_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_unsuspend_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_id_list: "aws_sdk_chime.types.user_id_list.UserIdList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.batch_unsuspend_user_response.BatchUnsuspendUserResponse":
        """<p>Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime <code>EnterpriseLWA</code> account. Only users on <code>EnterpriseLWA</code> accounts can be unsuspended using this action. For more information about different account types, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\"> Managing Your Amazon Chime Accounts </a> in the account types, in the <i>Amazon Chime Administration Guide</i>. </p> <p>Previously suspended users who are unsuspended using this action are returned to <code>Registered</code> status. Users who are not previously suspended are ignored.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id_list: <p>The request containing the user IDs to unsuspend.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.batch_unsuspend_user_request.BatchUnsuspendUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.batch_unsuspend_user_response.BatchUnsuspendUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.batch_unsuspend_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.batch_unsuspend_user.batch_unsuspend_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.batch_unsuspend_user_request.BatchUnsuspendUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id_list"] = user_id_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_phone_number(
        self,
        update_phone_number_request_items: "aws_sdk_chime.types.update_phone_number_request_item_list.UpdatePhoneNumberRequestItemList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse":
        """<p>Updates phone number product types or calling names. You can update one attribute at a time for each <code>UpdatePhoneNumberRequestItem</code>. For example, you can update the product type or the calling name.</p> <p>For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.</p> <p>Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.</p>

        Args:
            update_phone_number_request_items: <p>The request containing the phone number IDs and product types or calling names to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.batch_update_phone_number

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.batch_update_phone_number.batch_update_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest = {}  # type: ignore[typeddict-item]
        input_["update_phone_number_request_items"] = update_phone_number_request_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        update_user_request_items: "aws_sdk_chime.types.update_user_request_item_list.UpdateUserRequestItemList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.batch_update_user_response.BatchUpdateUserResponse":
        """<p>Updates user details within the <a>UpdateUserRequestItem</a> object for up to 20 users for the specified Amazon Chime account. Currently, only <code>LicenseType</code> updates are supported for this action.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            update_user_request_items: <p>The request containing the user IDs and details to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.batch_update_user_request.BatchUpdateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.batch_update_user_response.BatchUpdateUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.batch_update_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.batch_update_user.batch_update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.batch_update_user_request.BatchUpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["update_user_request_items"] = update_user_request_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_account(
        self,
        name: "aws_sdk_chime.types.account_name.AccountName",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.create_account_response.CreateAccountResponse":
        """<p>Creates an Amazon Chime account under the administrator's AWS account. Only <code>Team</code> account types are currently supported for this action. For more information about different account types, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\">Managing Your Amazon Chime Accounts</a> in the <i>Amazon Chime Administration Guide</i>.</p>

        Args:
            name: <p>The name of the Amazon Chime account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_account_request.CreateAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_account_response.CreateAccountResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_account

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_account.create_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_account_request.CreateAccountRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_bot(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        display_name: "aws_sdk_chime.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        domain: Optional["aws_sdk_chime.types.non_empty_string.NonEmptyString"] = None,
    ) -> "aws_sdk_chime.types.create_bot_response.CreateBotResponse":
        """<p>Creates a bot for an Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            display_name: <p>The bot display name.</p>
            domain: <p>The domain of the Amazon Chime Enterprise account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_bot_request.CreateBotRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_bot_response.CreateBotResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_bot

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_bot.create_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_bot_request.CreateBotRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["display_name"] = display_name
        if domain is not None:
            input_["domain"] = domain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_meeting_dial_out(
        self,
        meeting_id: "aws_sdk_chime.types.guid_string.GuidString",
        from_phone_number: "aws_sdk_chime.types.e164_phone_number.E164PhoneNumber",
        to_phone_number: "aws_sdk_chime.types.e164_phone_number.E164PhoneNumber",
        join_token: "aws_sdk_chime.types.join_token_string.JoinTokenString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.create_meeting_dial_out_response.CreateMeetingDialOutResponse":
        """<p>Uses the join token and call metadata in a meeting request (From number, To number, and so forth) to initiate an outbound call to a public switched telephone network (PSTN) and join them into a Chime meeting. Also ensures that the From number belongs to the customer.</p> <p>To play welcome audio or implement an interactive voice response (IVR), use the <code>CreateSipMediaApplicationCall</code> action with the corresponding SIP media application ID.</p> <important> <p> <b>This API is not available in a dedicated namespace.</b> </p> </important>

        Args:
            meeting_id: <p>The Amazon Chime SDK meeting ID.</p>
            from_phone_number: <p>Phone number used as the caller ID when the remote party receives a call.</p>
            to_phone_number: <p>Phone number called when inviting someone to a meeting.</p>
            join_token: <p>Token used by the Amazon Chime SDK attendee. Call the <a href=\"https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAttendee.html\">CreateAttendee</a> action to get a join token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_meeting_dial_out_request.CreateMeetingDialOutRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_meeting_dial_out_response.CreateMeetingDialOutResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_meeting_dial_out

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_meeting_dial_out.create_meeting_dial_out(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_meeting_dial_out_request.CreateMeetingDialOutRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["from_phone_number"] = from_phone_number
        input_["to_phone_number"] = to_phone_number
        input_["join_token"] = join_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_phone_number_order(
        self,
        product_type: "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType",
        e164_phone_numbers: "aws_sdk_chime.types.e164_phone_number_list.E164PhoneNumberList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.create_phone_number_order_response.CreatePhoneNumberOrderResponse":
        """<p>Creates an order for phone numbers to be provisioned. For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.</p>

        Args:
            product_type: <p>The phone number product type.</p>
            e164_phone_numbers: <p>List of phone numbers, in E.164 format.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_phone_number_order_request.CreatePhoneNumberOrderRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_phone_number_order_response.CreatePhoneNumberOrderResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_phone_number_order

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_phone_number_order.create_phone_number_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_phone_number_order_request.CreatePhoneNumberOrderRequest = {}  # type: ignore[typeddict-item]
        input_["product_type"] = product_type
        input_["e164_phone_numbers"] = e164_phone_numbers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_room(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        name: "aws_sdk_chime.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_chime.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_chime.types.create_room_response.CreateRoomResponse":
        """<p>Creates a chat room for the specified Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            name: <p>The room name.</p>
            client_request_token: <p>The idempotency token for the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_room_request.CreateRoomRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_room_response.CreateRoomResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_room

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_room.create_room(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_room_request.CreateRoomRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["name"] = name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_room_membership(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        member_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        role: Optional[
            "aws_sdk_chime.types.room_membership_role.RoomMembershipRole"
        ] = None,
    ) -> "aws_sdk_chime.types.create_room_membership_response.CreateRoomMembershipResponse":
        """<p>Adds a member to a chat room in an Amazon Chime Enterprise account. A member can be either a user or a bot. The member role designates whether the member is a chat room administrator or a general chat room member.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            member_id: <p>The Amazon Chime member ID (user ID or bot ID).</p>
            role: <p>The role of the member.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_room_membership_request.CreateRoomMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_room_membership_response.CreateRoomMembershipResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_room_membership

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_room_membership.create_room_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_room_membership_request.CreateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
        input_["member_id"] = member_id
        if role is not None:
            input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        username: Optional["aws_sdk_chime.types.string.String"] = None,
        email: Optional["aws_sdk_chime.types.email_address.EmailAddress"] = None,
        user_type: Optional["aws_sdk_chime.types.user_type.UserType"] = None,
    ) -> "aws_sdk_chime.types.create_user_response.CreateUserResponse":
        """<p>Creates a user under the specified Amazon Chime account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            username: <p>The user name.</p>
            email: <p>The user's email address.</p>
            user_type: <p>The user type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.create_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        if username is not None:
            input_["username"] = username
        if email is not None:
            input_["email"] = email
        if user_type is not None:
            input_["user_type"] = user_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_account(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.delete_account_response.DeleteAccountResponse":
        """<p>Deletes the specified Amazon Chime account. You must suspend all users before deleting <code>Team</code> account. You can use the <a>BatchSuspendUser</a> action to dodo.</p> <p>For <code>EnterpriseLWA</code> and <code>EnterpriseAD</code> accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.</p> <p>Deleted accounts appear in your <code>Disabled</code> accounts list for 90 days. To restore deleted account from your <code>Disabled</code> accounts list, you must contact AWS Support.</p> <p>After 90 days, deleted accounts are permanently removed from your <code>Disabled</code> accounts list.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.delete_account_request.DeleteAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.delete_account_response.DeleteAccountResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.delete_account

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.delete_account.delete_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.delete_account_request.DeleteAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_events_configuration(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> None:
        """<p>Deletes the events configuration that allows a bot to receive outgoing events.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            bot_id: <p>The bot ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.delete_events_configuration_request.DeleteEventsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.delete_events_configuration

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.delete_events_configuration.delete_events_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.delete_events_configuration_request.DeleteEventsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["bot_id"] = bot_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_phone_number(
        self,
        phone_number_id: "aws_sdk_chime.types.string.String",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> None:
        """<p>Moves the specified phone number into the <b>Deletion queue</b>. A phone number must be disassociated from any users or Amazon Chime Voice Connectors before it can be deleted.</p> <p>Deleted phone numbers remain in the <b>Deletion queue</b> for 7 days before they are deleted permanently.</p>

        Args:
            phone_number_id: <p>The phone number ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.delete_phone_number_request.DeletePhoneNumberRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.delete_phone_number

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.delete_phone_number.delete_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.delete_phone_number_request.DeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
        input_["phone_number_id"] = phone_number_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_room(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> None:
        """<p>Deletes a chat room in an Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The chat room ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.delete_room_request.DeleteRoomRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.delete_room

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.delete_room.delete_room(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.delete_room_request.DeleteRoomRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_room_membership(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        member_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> None:
        """<p>Removes a member from a chat room in an Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            member_id: <p>The member ID (user ID or bot ID).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.delete_room_membership_request.DeleteRoomMembershipRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.delete_room_membership

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.delete_room_membership.delete_room_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.delete_room_membership_request.DeleteRoomMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
        input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_phone_number_from_user(
        self,
        account_id: "aws_sdk_chime.types.string.String",
        user_id: "aws_sdk_chime.types.string.String",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.disassociate_phone_number_from_user_response.DisassociatePhoneNumberFromUserResponse":
        """<p>Disassociates the primary provisioned phone number from the specified Amazon Chime user.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.disassociate_phone_number_from_user_request.DisassociatePhoneNumberFromUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.disassociate_phone_number_from_user_response.DisassociatePhoneNumberFromUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.disassociate_phone_number_from_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.disassociate_phone_number_from_user.disassociate_phone_number_from_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.disassociate_phone_number_from_user_request.DisassociatePhoneNumberFromUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_signin_delegate_groups_from_account(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        group_names: "aws_sdk_chime.types.non_empty_string_list.NonEmptyStringList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.disassociate_signin_delegate_groups_from_account_response.DisassociateSigninDelegateGroupsFromAccountResponse":
        """<p>Disassociates the specified sign-in delegate groups from the specified Amazon Chime account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            group_names: <p>The sign-in delegate group names.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.disassociate_signin_delegate_groups_from_account_request.DisassociateSigninDelegateGroupsFromAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.disassociate_signin_delegate_groups_from_account_response.DisassociateSigninDelegateGroupsFromAccountResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.disassociate_signin_delegate_groups_from_account

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.disassociate_signin_delegate_groups_from_account.disassociate_signin_delegate_groups_from_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.disassociate_signin_delegate_groups_from_account_request.DisassociateSigninDelegateGroupsFromAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["group_names"] = group_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_account(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_account_response.GetAccountResponse":
        """<p>Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_account_request.GetAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_account_response.GetAccountResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_account

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_account.get_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_account_request.GetAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_account_settings(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dialout settings. For more information about these settings, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/policies.html\">Use the Policies Page</a> in the <i>Amazon Chime Administration Guide</i>. </p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_account_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_account_settings_request.GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_bot(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_bot_response.GetBotResponse":
        """<p>Retrieves details for the specified bot, such as bot email address, bot type, status, and display name.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            bot_id: <p>The bot ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_bot_request.GetBotRequest]",
        ) -> OperationResponse["aws_sdk_chime.types.get_bot_response.GetBotResponse"]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_bot

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_bot.get_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_bot_request.GetBotRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["bot_id"] = bot_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_events_configuration(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_events_configuration_response.GetEventsConfigurationResponse":
        """<p>Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            bot_id: <p>The bot ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_events_configuration_request.GetEventsConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_events_configuration_response.GetEventsConfigurationResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_events_configuration

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_events_configuration.get_events_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_events_configuration_request.GetEventsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["bot_id"] = bot_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_global_settings(
        self, *, config_overrides: Optional[ChimeClientConfig] = None
    ) -> "aws_sdk_chime.types.get_global_settings_response.GetGlobalSettingsResponse":
        """<p>Retrieves global settings for the administrator's AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.</p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_global_settings_response.GetGlobalSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_global_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_global_settings.get_global_settings(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_phone_number(
        self,
        phone_number_id: "aws_sdk_chime.types.string.String",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_phone_number_response.GetPhoneNumberResponse":
        """<p>Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.</p>

        Args:
            phone_number_id: <p>The phone number ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_phone_number_request.GetPhoneNumberRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_phone_number_response.GetPhoneNumberResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_phone_number

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_phone_number.get_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_phone_number_request.GetPhoneNumberRequest = {}  # type: ignore[typeddict-item]
        input_["phone_number_id"] = phone_number_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_phone_number_order(
        self,
        phone_number_order_id: "aws_sdk_chime.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_phone_number_order_response.GetPhoneNumberOrderResponse":
        """<p>Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.</p>

        Args:
            phone_number_order_id: <p>The ID for the phone number order.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_phone_number_order_request.GetPhoneNumberOrderRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_phone_number_order_response.GetPhoneNumberOrderResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_phone_number_order

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_phone_number_order.get_phone_number_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_phone_number_order_request.GetPhoneNumberOrderRequest = {}  # type: ignore[typeddict-item]
        input_["phone_number_order_id"] = phone_number_order_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_phone_number_settings(
        self, *, config_overrides: Optional[ChimeClientConfig] = None
    ) -> "aws_sdk_chime.types.get_phone_number_settings_response.GetPhoneNumberSettingsResponse":
        """<p>Retrieves the phone number settings for the administrator's AWS account, such as the default outbound calling name.</p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_phone_number_settings_response.GetPhoneNumberSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_phone_number_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_phone_number_settings.get_phone_number_settings(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_retention_settings(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_retention_settings_response.GetRetentionSettingsResponse":
        """<p> Gets the retention settings for the specified Amazon Chime Enterprise account. For more information about retention settings, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\">Managing Chat Retention Policies</a> in the <i>Amazon Chime Administration Guide</i>. </p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_retention_settings_request.GetRetentionSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_retention_settings_response.GetRetentionSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_retention_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_retention_settings.get_retention_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_retention_settings_request.GetRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_room(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_room_response.GetRoomResponse":
        """<p>Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_room_request.GetRoomRequest]",
        ) -> OperationResponse["aws_sdk_chime.types.get_room_response.GetRoomResponse"]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_room

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_room.get_room(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_room_request.GetRoomRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_user_response.GetUserResponse":
        """<p>Retrieves details for the specified user ID, such as primary email address, license type,and personal meeting PIN.</p> <p> To retrieve user details with an email address instead of a user ID, use the <a>ListUsers</a> action, and then filter by email address. </p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_user_request.GetUserRequest]",
        ) -> OperationResponse["aws_sdk_chime.types.get_user_response.GetUserResponse"]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_user.get_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_user_request.GetUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_user_settings(
        self,
        account_id: "aws_sdk_chime.types.string.String",
        user_id: "aws_sdk_chime.types.string.String",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.get_user_settings_response.GetUserSettingsResponse":
        """<p>Retrieves settings for the specified user ID, such as any associated phone number settings.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.get_user_settings_request.GetUserSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.get_user_settings_response.GetUserSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.get_user_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.get_user_settings.get_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.get_user_settings_request.GetUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def invite_users(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_email_list: "aws_sdk_chime.types.user_email_list.UserEmailList",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        user_type: Optional["aws_sdk_chime.types.user_type.UserType"] = None,
    ) -> "aws_sdk_chime.types.invite_users_response.InviteUsersResponse":
        """<p>Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime <code>Team</code> account. Only <code>Team</code> account types are currently supported for this action.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_email_list: <p>The user email addresses to which to send the email invitation.</p>
            user_type: <p>The user type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.invite_users_request.InviteUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.invite_users_response.InviteUsersResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.invite_users

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.invite_users.invite_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.invite_users_request.InviteUsersRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_email_list"] = user_email_list
        if user_type is not None:
            input_["user_type"] = user_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_accounts(
        self,
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        name: Optional["aws_sdk_chime.types.account_name.AccountName"] = None,
        user_email: Optional["aws_sdk_chime.types.email_address.EmailAddress"] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_chime.types.profile_service_max_results.ProfileServiceMaxResults"
        ] = None,
    ) -> "aws_sdk_chime.types.list_accounts_response.ListAccountsResponse":
        """<p>Lists the Amazon Chime accounts under the administrator's AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user's email address, which returns one account result.</p>

        Args:
            name: <p>Amazon Chime account name prefix with which to filter results.</p>
            user_email: <p>User email address with which to filter results.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. Defaults to 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_accounts_request.ListAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_accounts_response.ListAccountsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_accounts

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_accounts.list_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_accounts_request.ListAccountsRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if user_email is not None:
            input_["user_email"] = user_email
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

    def list_bots(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        max_results: Optional["aws_sdk_chime.types.result_max.ResultMax"] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
    ) -> "aws_sdk_chime.types.list_bots_response.ListBotsResponse":
        """<p>Lists the bots associated with the administrator's Amazon Chime Enterprise account ID.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            max_results: <p>The maximum number of results to return in a single call. The default is 10.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_bots_request.ListBotsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_bots_response.ListBotsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_bots

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_bots.list_bots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_bots_request.ListBotsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
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

    def list_phone_number_orders(
        self,
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
        max_results: Optional["aws_sdk_chime.types.result_max.ResultMax"] = None,
    ) -> "aws_sdk_chime.types.list_phone_number_orders_response.ListPhoneNumberOrdersResponse":
        """<p>Lists the phone number orders for the administrator's Amazon Chime account.</p>

        Args:
            next_token: <p>The token to use to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_phone_number_orders_request.ListPhoneNumberOrdersRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_phone_number_orders_response.ListPhoneNumberOrdersResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_phone_number_orders

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_phone_number_orders.list_phone_number_orders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_phone_number_orders_request.ListPhoneNumberOrdersRequest = {}  # type: ignore[typeddict-item]
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

    def list_phone_numbers(
        self,
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        status: Optional[
            "aws_sdk_chime.types.phone_number_status.PhoneNumberStatus"
        ] = None,
        product_type: Optional[
            "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType"
        ] = None,
        filter_name: Optional[
            "aws_sdk_chime.types.phone_number_association_name.PhoneNumberAssociationName"
        ] = None,
        filter_value: Optional["aws_sdk_chime.types.string.String"] = None,
        max_results: Optional["aws_sdk_chime.types.result_max.ResultMax"] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
    ) -> "aws_sdk_chime.types.list_phone_numbers_response.ListPhoneNumbersResponse":
        """<p>Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.</p>

        Args:
            status: <p>The phone number status.</p>
            product_type: <p>The phone number product type.</p>
            filter_name: <p>The filter to use to limit the number of results.</p>
            filter_value: <p>The value to use for the filter.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_phone_numbers_request.ListPhoneNumbersRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_phone_numbers_response.ListPhoneNumbersResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_phone_numbers

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_phone_numbers.list_phone_numbers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_phone_numbers_request.ListPhoneNumbersRequest = {}  # type: ignore[typeddict-item]
        if status is not None:
            input_["status"] = status
        if product_type is not None:
            input_["product_type"] = product_type
        if filter_name is not None:
            input_["filter_name"] = filter_name
        if filter_value is not None:
            input_["filter_value"] = filter_value
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

    def list_room_memberships(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        max_results: Optional["aws_sdk_chime.types.result_max.ResultMax"] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
    ) -> (
        "aws_sdk_chime.types.list_room_memberships_response.ListRoomMembershipsResponse"
    ):
        """<p>Lists the membership details for the specified room in an Amazon Chime Enterprise account, such as the members' IDs, email addresses, and names.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_room_memberships_request.ListRoomMembershipsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_room_memberships_response.ListRoomMembershipsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_room_memberships

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_room_memberships.list_room_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_room_memberships_request.ListRoomMembershipsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
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

    def list_rooms(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        member_id: Optional["aws_sdk_chime.types.string.String"] = None,
        max_results: Optional["aws_sdk_chime.types.result_max.ResultMax"] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
    ) -> "aws_sdk_chime.types.list_rooms_response.ListRoomsResponse":
        """<p>Lists the room details for the specified Amazon Chime Enterprise account. Optionally, filter the results by a member ID (user ID or bot ID) to see a list of rooms that the member belongs to.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            member_id: <p>The member ID (user ID or bot ID).</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_rooms_request.ListRoomsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_rooms_response.ListRoomsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_rooms

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_rooms.list_rooms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_rooms_request.ListRoomsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        if member_id is not None:
            input_["member_id"] = member_id
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

    def list_supported_phone_number_countries(
        self,
        product_type: "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.list_supported_phone_number_countries_response.ListSupportedPhoneNumberCountriesResponse":
        """<p>Lists supported phone number countries.</p>

        Args:
            product_type: <p>The phone number product type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_supported_phone_number_countries_request.ListSupportedPhoneNumberCountriesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_supported_phone_number_countries_response.ListSupportedPhoneNumberCountriesResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_supported_phone_number_countries

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_supported_phone_number_countries.list_supported_phone_number_countries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_supported_phone_number_countries_request.ListSupportedPhoneNumberCountriesRequest = {}  # type: ignore[typeddict-item]
        input_["product_type"] = product_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_users(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        user_email: Optional["aws_sdk_chime.types.email_address.EmailAddress"] = None,
        user_type: Optional["aws_sdk_chime.types.user_type.UserType"] = None,
        max_results: Optional[
            "aws_sdk_chime.types.profile_service_max_results.ProfileServiceMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
    ) -> "aws_sdk_chime.types.list_users_response.ListUsersResponse":
        """<p>Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_email: <p>Optional. The user email address used to filter results. Maximum 1.</p>
            user_type: <p>The user type.</p>
            max_results: <p>The maximum number of results to return in a single call. Defaults to 100.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.list_users_response.ListUsersResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.list_users

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.list_users_request.ListUsersRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        if user_email is not None:
            input_["user_email"] = user_email
        if user_type is not None:
            input_["user_type"] = user_type
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

    def logout_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.logout_user_response.LogoutUserResponse":
        """<p>Logs out the specified user from all of the devices they are currently logged into.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.logout_user_request.LogoutUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.logout_user_response.LogoutUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.logout_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.logout_user.logout_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.logout_user_request.LogoutUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_events_configuration(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        outbound_events_https_endpoint: Optional[
            "aws_sdk_chime.types.sensitive_string.SensitiveString"
        ] = None,
        lambda_function_arn: Optional[
            "aws_sdk_chime.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "aws_sdk_chime.types.put_events_configuration_response.PutEventsConfigurationResponse":
        """<p>Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime. Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see <a>Bot</a>.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            bot_id: <p>The bot ID.</p>
            outbound_events_https_endpoint: <p>HTTPS endpoint that allows the bot to receive outgoing events.</p>
            lambda_function_arn: <p>Lambda function ARN that allows the bot to receive outgoing events.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.put_events_configuration_request.PutEventsConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.put_events_configuration_response.PutEventsConfigurationResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.put_events_configuration

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.put_events_configuration.put_events_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.put_events_configuration_request.PutEventsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["bot_id"] = bot_id
        if outbound_events_https_endpoint is not None:
            input_["outbound_events_https_endpoint"] = outbound_events_https_endpoint
        if lambda_function_arn is not None:
            input_["lambda_function_arn"] = lambda_function_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_retention_settings(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        retention_settings: "aws_sdk_chime.types.retention_settings.RetentionSettings",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.put_retention_settings_response.PutRetentionSettingsResponse":
        """<p> Puts retention settings for the specified Amazon Chime Enterprise account. We recommend using AWS CloudTrail to monitor usage of this API for your account. For more information, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/cloudtrail.html\">Logging Amazon Chime API Calls with AWS CloudTrail</a> in the <i>Amazon Chime Administration Guide</i>.</p> <p> To turn off existing retention settings, remove the number of days from the corresponding <b>RetentionDays</b> field in the <b>RetentionSettings</b> object. For more information about retention settings, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\">Managing Chat Retention Policies</a> in the <i>Amazon Chime Administration Guide</i>.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            retention_settings: <p>The retention settings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.put_retention_settings_request.PutRetentionSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.put_retention_settings_response.PutRetentionSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.put_retention_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.put_retention_settings.put_retention_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.put_retention_settings_request.PutRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["retention_settings"] = retention_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def redact_conversation_message(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        conversation_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        message_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.redact_conversation_message_response.RedactConversationMessageResponse":
        """<p>Redacts the specified message from the specified Amazon Chime conversation.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            conversation_id: <p>The conversation ID.</p>
            message_id: <p>The message ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.redact_conversation_message_request.RedactConversationMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.redact_conversation_message_response.RedactConversationMessageResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.redact_conversation_message

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.redact_conversation_message.redact_conversation_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.redact_conversation_message_request.RedactConversationMessageRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["conversation_id"] = conversation_id
        input_["message_id"] = message_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def redact_room_message(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        message_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.redact_room_message_response.RedactRoomMessageResponse":
        """<p>Redacts the specified message from the specified Amazon Chime channel.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            message_id: <p>The message ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.redact_room_message_request.RedactRoomMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.redact_room_message_response.RedactRoomMessageResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.redact_room_message

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.redact_room_message.redact_room_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.redact_room_message_request.RedactRoomMessageRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
        input_["message_id"] = message_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def regenerate_security_token(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.regenerate_security_token_response.RegenerateSecurityTokenResponse":
        """<p>Regenerates the security token for a bot.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            bot_id: <p>The bot ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.regenerate_security_token_request.RegenerateSecurityTokenRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.regenerate_security_token_response.RegenerateSecurityTokenResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.regenerate_security_token

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.regenerate_security_token.regenerate_security_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.regenerate_security_token_request.RegenerateSecurityTokenRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["bot_id"] = bot_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reset_personal_pin(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.reset_personal_pin_response.ResetPersonalPINResponse":
        """<p>Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the <a>User</a> object with the updated personal meeting PIN.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.reset_personal_pin_request.ResetPersonalPINRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.reset_personal_pin_response.ResetPersonalPINResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.reset_personal_pin

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.reset_personal_pin.reset_personal_pin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.reset_personal_pin_request.ResetPersonalPINRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restore_phone_number(
        self,
        phone_number_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.restore_phone_number_response.RestorePhoneNumberResponse":
        """<p>Moves a phone number from the <b>Deletion queue</b> back into the phone number <b>Inventory</b>.</p>

        Args:
            phone_number_id: <p>The phone number.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.restore_phone_number_request.RestorePhoneNumberRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.restore_phone_number_response.RestorePhoneNumberResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.restore_phone_number

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.restore_phone_number.restore_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.restore_phone_number_request.RestorePhoneNumberRequest = {}  # type: ignore[typeddict-item]
        input_["phone_number_id"] = phone_number_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_available_phone_numbers(
        self,
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        area_code: Optional["aws_sdk_chime.types.string.String"] = None,
        city: Optional["aws_sdk_chime.types.string.String"] = None,
        country: Optional[
            "aws_sdk_chime.types.alpha2_country_code.Alpha2CountryCode"
        ] = None,
        state: Optional["aws_sdk_chime.types.string.String"] = None,
        toll_free_prefix: Optional[
            "aws_sdk_chime.types.toll_free_prefix.TollFreePrefix"
        ] = None,
        phone_number_type: Optional[
            "aws_sdk_chime.types.phone_number_type.PhoneNumberType"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime.types.phone_number_max_results.PhoneNumberMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_chime.types.string.String"] = None,
    ) -> "aws_sdk_chime.types.search_available_phone_numbers_response.SearchAvailablePhoneNumbersResponse":
        """<p>Searches for phone numbers that can be ordered. For US numbers, provide at least one of the following search filters: <code>AreaCode</code>, <code>City</code>, <code>State</code>, or <code>TollFreePrefix</code>. If you provide <code>City</code>, you must also provide <code>State</code>. Numbers outside the US only support the <code>PhoneNumberType</code> filter, which you must use.</p>

        Args:
            area_code: <p>The area code used to filter results. Only applies to the US.</p>
            city: <p>The city used to filter results. Only applies to the US.</p>
            country: <p>The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2.</p>
            state: <p>The state used to filter results. Required only if you provide <code>City</code>. Only applies to the US.</p>
            toll_free_prefix: <p>The toll-free prefix that you use to filter results. Only applies to the US.</p>
            phone_number_type: <p>The phone number type used to filter results. Required for non-US numbers.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token used to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.search_available_phone_numbers_request.SearchAvailablePhoneNumbersRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.search_available_phone_numbers_response.SearchAvailablePhoneNumbersResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.search_available_phone_numbers

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.search_available_phone_numbers.search_available_phone_numbers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.search_available_phone_numbers_request.SearchAvailablePhoneNumbersRequest = {}  # type: ignore[typeddict-item]
        if area_code is not None:
            input_["area_code"] = area_code
        if city is not None:
            input_["city"] = city
        if country is not None:
            input_["country"] = country
        if state is not None:
            input_["state"] = state
        if toll_free_prefix is not None:
            input_["toll_free_prefix"] = toll_free_prefix
        if phone_number_type is not None:
            input_["phone_number_type"] = phone_number_type
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

    def update_account(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        name: Optional["aws_sdk_chime.types.account_name.AccountName"] = None,
        default_license: Optional["aws_sdk_chime.types.license.License"] = None,
    ) -> "aws_sdk_chime.types.update_account_response.UpdateAccountResponse":
        """<p>Updates account details for the specified Amazon Chime account. Currently, only account name and default license updates are supported for this action.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            name: <p>The new name for the specified Amazon Chime account.</p>
            default_license: <p>The default license applied when you add users to an Amazon Chime account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_account_request.UpdateAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_account_response.UpdateAccountResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_account

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_account.update_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_account_request.UpdateAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        if name is not None:
            input_["name"] = name
        if default_license is not None:
            input_["default_license"] = default_license

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_account_settings(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        account_settings: "aws_sdk_chime.types.account_settings.AccountSettings",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> "aws_sdk_chime.types.update_account_settings_response.UpdateAccountSettingsResponse":
        """<p>Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see <a href=\"https://docs.aws.amazon.com/chime/latest/ag/policies.html\">Use the Policies Page</a> in the <i>Amazon Chime Administration Guide</i>.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            account_settings: <p>The Amazon Chime account settings to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_account_settings_request.UpdateAccountSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_account_settings_response.UpdateAccountSettingsResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_account_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_account_settings.update_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_account_settings_request.UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["account_settings"] = account_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_bot(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        bot_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        disabled: Optional[
            "aws_sdk_chime.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_chime.types.update_bot_response.UpdateBotResponse":
        """<p>Updates the status of the specified bot, such as starting or stopping the bot from running in your Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            bot_id: <p>The bot ID.</p>
            disabled: <p>When true, stops the specified bot from running in your account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_bot_request.UpdateBotRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_bot_response.UpdateBotResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_bot

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_bot.update_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_bot_request.UpdateBotRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["bot_id"] = bot_id
        if disabled is not None:
            input_["disabled"] = disabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_global_settings(
        self,
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        business_calling: Optional[
            "aws_sdk_chime.types.business_calling_settings.BusinessCallingSettings"
        ] = None,
        voice_connector: Optional[
            "aws_sdk_chime.types.voice_connector_settings.VoiceConnectorSettings"
        ] = None,
    ) -> None:
        """<p>Updates global settings for the administrator's AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.</p>

        Args:
            business_calling: <p>The Amazon Chime Business Calling settings.</p>
            voice_connector: <p>The Amazon Chime Voice Connector settings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_global_settings_request.UpdateGlobalSettingsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_global_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_global_settings.update_global_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_global_settings_request.UpdateGlobalSettingsRequest = {}  # type: ignore[typeddict-item]
        if business_calling is not None:
            input_["business_calling"] = business_calling
        if voice_connector is not None:
            input_["voice_connector"] = voice_connector

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_phone_number(
        self,
        phone_number_id: "aws_sdk_chime.types.string.String",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        product_type: Optional[
            "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType"
        ] = None,
        calling_name: Optional["aws_sdk_chime.types.calling_name.CallingName"] = None,
    ) -> "aws_sdk_chime.types.update_phone_number_response.UpdatePhoneNumberResponse":
        """<p>Updates phone number details, such as product type or calling name, for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type or the calling name in one action.</p> <p>For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.</p> <p>Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.</p>

        Args:
            phone_number_id: <p>The phone number ID.</p>
            product_type: <p>The product type.</p>
            calling_name: <p>The outbound calling name associated with the phone number.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_phone_number_request.UpdatePhoneNumberRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_phone_number_response.UpdatePhoneNumberResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_phone_number

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_phone_number.update_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_phone_number_request.UpdatePhoneNumberRequest = {}  # type: ignore[typeddict-item]
        input_["phone_number_id"] = phone_number_id
        if product_type is not None:
            input_["product_type"] = product_type
        if calling_name is not None:
            input_["calling_name"] = calling_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_phone_number_settings(
        self,
        calling_name: "aws_sdk_chime.types.calling_name.CallingName",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> None:
        """<p>Updates the phone number settings for the administrator's AWS account, such as the default outbound calling name. You can update the default outbound calling name once every seven days. Outbound calling names can take up to 72 hours to update.</p>

        Args:
            calling_name: <p>The default outbound calling name for the account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_phone_number_settings_request.UpdatePhoneNumberSettingsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_phone_number_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_phone_number_settings.update_phone_number_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_phone_number_settings_request.UpdatePhoneNumberSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["calling_name"] = calling_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_room(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        name: Optional["aws_sdk_chime.types.sensitive_string.SensitiveString"] = None,
    ) -> "aws_sdk_chime.types.update_room_response.UpdateRoomResponse":
        """<p>Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            name: <p>The room name.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_room_request.UpdateRoomRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_room_response.UpdateRoomResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_room

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_room.update_room(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_room_request.UpdateRoomRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_room_membership(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        member_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        role: Optional[
            "aws_sdk_chime.types.room_membership_role.RoomMembershipRole"
        ] = None,
    ) -> "aws_sdk_chime.types.update_room_membership_response.UpdateRoomMembershipResponse":
        """<p>Updates room membership details, such as the member role, for a room in an Amazon Chime Enterprise account. The member role designates whether the member is a chat room administrator or a general chat room member. The member role can be updated only for user IDs.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            room_id: <p>The room ID.</p>
            member_id: <p>The member ID.</p>
            role: <p>The role of the member.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_room_membership_request.UpdateRoomMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_room_membership_response.UpdateRoomMembershipResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_room_membership

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_room_membership.update_room_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_room_membership_request.UpdateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["room_id"] = room_id
        input_["member_id"] = member_id
        if role is not None:
            input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_user(
        self,
        account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
        license_type: Optional["aws_sdk_chime.types.license.License"] = None,
        user_type: Optional["aws_sdk_chime.types.user_type.UserType"] = None,
        alexa_for_business_metadata: Optional[
            "aws_sdk_chime.types.alexa_for_business_metadata.AlexaForBusinessMetadata"
        ] = None,
    ) -> "aws_sdk_chime.types.update_user_response.UpdateUserResponse":
        """<p>Updates user details for a specified user ID. Currently, only <code>LicenseType</code> updates are supported for this action.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
            license_type: <p>The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to.</p>
            user_type: <p>The user type.</p>
            alexa_for_business_metadata: <p>The Alexa for Business metadata.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_user

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id
        if license_type is not None:
            input_["license_type"] = license_type
        if user_type is not None:
            input_["user_type"] = user_type
        if alexa_for_business_metadata is not None:
            input_["alexa_for_business_metadata"] = alexa_for_business_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_user_settings(
        self,
        account_id: "aws_sdk_chime.types.string.String",
        user_id: "aws_sdk_chime.types.string.String",
        user_settings: "aws_sdk_chime.types.user_settings.UserSettings",
        *,
        config_overrides: Optional[ChimeClientConfig] = None,
    ) -> None:
        """<p>Updates the settings for the specified user, such as phone number settings.</p>

        Args:
            account_id: <p>The Amazon Chime account ID.</p>
            user_id: <p>The user ID.</p>
            user_settings: <p>The user settings to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime.types.update_user_settings_request.UpdateUserSettingsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime._operations.uc_buzz_console_service.update_user_settings

            output, http_response = (
                aws_sdk_chime._operations.uc_buzz_console_service.update_user_settings.update_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime.types.update_user_settings_request.UpdateUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["user_id"] = user_id
        input_["user_settings"] = user_settings

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
