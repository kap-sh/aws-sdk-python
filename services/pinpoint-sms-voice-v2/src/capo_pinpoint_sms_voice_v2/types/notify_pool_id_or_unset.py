"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyPoolIdOrUnset``."""

from typing import TypeAlias

"""A pool identifier (ID or ARN) or the special value UNSET_DEFAULT_POOL_FOR_NOTIFY. Pass UNSET_DEFAULT_POOL_FOR_NOTIFY to clear the default pool from a NotifyConfiguration. This shape is used exclusively in UpdateNotifyConfigurationRequest."""
NotifyPoolIdOrUnset: TypeAlias = str
