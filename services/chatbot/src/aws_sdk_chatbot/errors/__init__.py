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
from ._base import (
    chatbotError as chatbotError,
)
from .conflict_exception import ConflictException as ConflictException
from .create_chime_webhook_configuration_exception import (
    CreateChimeWebhookConfigurationException as CreateChimeWebhookConfigurationException,
)
from .create_slack_channel_configuration_exception import (
    CreateSlackChannelConfigurationException as CreateSlackChannelConfigurationException,
)
from .create_teams_channel_configuration_exception import (
    CreateTeamsChannelConfigurationException as CreateTeamsChannelConfigurationException,
)
from .delete_chime_webhook_configuration_exception import (
    DeleteChimeWebhookConfigurationException as DeleteChimeWebhookConfigurationException,
)
from .delete_microsoft_teams_user_identity_exception import (
    DeleteMicrosoftTeamsUserIdentityException as DeleteMicrosoftTeamsUserIdentityException,
)
from .delete_slack_channel_configuration_exception import (
    DeleteSlackChannelConfigurationException as DeleteSlackChannelConfigurationException,
)
from .delete_slack_user_identity_exception import (
    DeleteSlackUserIdentityException as DeleteSlackUserIdentityException,
)
from .delete_slack_workspace_authorization_fault import (
    DeleteSlackWorkspaceAuthorizationFault as DeleteSlackWorkspaceAuthorizationFault,
)
from .delete_teams_channel_configuration_exception import (
    DeleteTeamsChannelConfigurationException as DeleteTeamsChannelConfigurationException,
)
from .delete_teams_configured_team_exception import (
    DeleteTeamsConfiguredTeamException as DeleteTeamsConfiguredTeamException,
)
from .describe_chime_webhook_configurations_exception import (
    DescribeChimeWebhookConfigurationsException as DescribeChimeWebhookConfigurationsException,
)
from .describe_slack_channel_configurations_exception import (
    DescribeSlackChannelConfigurationsException as DescribeSlackChannelConfigurationsException,
)
from .describe_slack_user_identities_exception import (
    DescribeSlackUserIdentitiesException as DescribeSlackUserIdentitiesException,
)
from .describe_slack_workspaces_exception import (
    DescribeSlackWorkspacesException as DescribeSlackWorkspacesException,
)
from .get_account_preferences_exception import (
    GetAccountPreferencesException as GetAccountPreferencesException,
)
from .get_teams_channel_configuration_exception import (
    GetTeamsChannelConfigurationException as GetTeamsChannelConfigurationException,
)
from .internal_service_error import InternalServiceError as InternalServiceError
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .list_microsoft_teams_configured_teams_exception import (
    ListMicrosoftTeamsConfiguredTeamsException as ListMicrosoftTeamsConfiguredTeamsException,
)
from .list_microsoft_teams_user_identities_exception import (
    ListMicrosoftTeamsUserIdentitiesException as ListMicrosoftTeamsUserIdentitiesException,
)
from .list_teams_channel_configurations_exception import (
    ListTeamsChannelConfigurationsException as ListTeamsChannelConfigurationsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .update_account_preferences_exception import (
    UpdateAccountPreferencesException as UpdateAccountPreferencesException,
)
from .update_chime_webhook_configuration_exception import (
    UpdateChimeWebhookConfigurationException as UpdateChimeWebhookConfigurationException,
)
from .update_slack_channel_configuration_exception import (
    UpdateSlackChannelConfigurationException as UpdateSlackChannelConfigurationException,
)
from .update_teams_channel_configuration_exception import (
    UpdateTeamsChannelConfigurationException as UpdateTeamsChannelConfigurationException,
)
