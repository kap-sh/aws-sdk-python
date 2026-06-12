from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .account_sending_paused_exception import (
    AccountSendingPausedException as AccountSendingPausedException,
)
from .already_exists_exception import AlreadyExistsException as AlreadyExistsException
from .cannot_delete_exception import CannotDeleteException as CannotDeleteException
from .configuration_set_already_exists_exception import (
    ConfigurationSetAlreadyExistsException as ConfigurationSetAlreadyExistsException,
)
from .configuration_set_does_not_exist_exception import (
    ConfigurationSetDoesNotExistException as ConfigurationSetDoesNotExistException,
)
from .configuration_set_sending_paused_exception import (
    ConfigurationSetSendingPausedException as ConfigurationSetSendingPausedException,
)
from .custom_verification_email_invalid_content_exception import (
    CustomVerificationEmailInvalidContentException as CustomVerificationEmailInvalidContentException,
)
from .custom_verification_email_template_already_exists_exception import (
    CustomVerificationEmailTemplateAlreadyExistsException as CustomVerificationEmailTemplateAlreadyExistsException,
)
from .custom_verification_email_template_does_not_exist_exception import (
    CustomVerificationEmailTemplateDoesNotExistException as CustomVerificationEmailTemplateDoesNotExistException,
)
from .event_destination_already_exists_exception import (
    EventDestinationAlreadyExistsException as EventDestinationAlreadyExistsException,
)
from .event_destination_does_not_exist_exception import (
    EventDestinationDoesNotExistException as EventDestinationDoesNotExistException,
)
from .from_email_address_not_verified_exception import (
    FromEmailAddressNotVerifiedException as FromEmailAddressNotVerifiedException,
)
from .invalid_cloud_watch_destination_exception import (
    InvalidCloudWatchDestinationException as InvalidCloudWatchDestinationException,
)
from .invalid_configuration_set_exception import (
    InvalidConfigurationSetException as InvalidConfigurationSetException,
)
from .invalid_delivery_options_exception import (
    InvalidDeliveryOptionsException as InvalidDeliveryOptionsException,
)
from .invalid_firehose_destination_exception import (
    InvalidFirehoseDestinationException as InvalidFirehoseDestinationException,
)
from .invalid_lambda_function_exception import (
    InvalidLambdaFunctionException as InvalidLambdaFunctionException,
)
from .invalid_policy_exception import InvalidPolicyException as InvalidPolicyException
from .invalid_rendering_parameter_exception import (
    InvalidRenderingParameterException as InvalidRenderingParameterException,
)
from .invalid_s3_configuration_exception import (
    InvalidS3ConfigurationException as InvalidS3ConfigurationException,
)
from .invalid_sns_destination_exception import (
    InvalidSNSDestinationException as InvalidSNSDestinationException,
)
from .invalid_sns_topic_exception import (
    InvalidSnsTopicException as InvalidSnsTopicException,
)
from .invalid_template_exception import (
    InvalidTemplateException as InvalidTemplateException,
)
from .invalid_tracking_options_exception import (
    InvalidTrackingOptionsException as InvalidTrackingOptionsException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .mail_from_domain_not_verified_exception import (
    MailFromDomainNotVerifiedException as MailFromDomainNotVerifiedException,
)
from .message_rejected import MessageRejected as MessageRejected
from .missing_rendering_attribute_exception import (
    MissingRenderingAttributeException as MissingRenderingAttributeException,
)
from .production_access_not_granted_exception import (
    ProductionAccessNotGrantedException as ProductionAccessNotGrantedException,
)
from .rule_does_not_exist_exception import (
    RuleDoesNotExistException as RuleDoesNotExistException,
)
from .rule_set_does_not_exist_exception import (
    RuleSetDoesNotExistException as RuleSetDoesNotExistException,
)
from .template_does_not_exist_exception import (
    TemplateDoesNotExistException as TemplateDoesNotExistException,
)
from .tracking_options_already_exists_exception import (
    TrackingOptionsAlreadyExistsException as TrackingOptionsAlreadyExistsException,
)
from .tracking_options_does_not_exist_exception import (
    TrackingOptionsDoesNotExistException as TrackingOptionsDoesNotExistException,
)
