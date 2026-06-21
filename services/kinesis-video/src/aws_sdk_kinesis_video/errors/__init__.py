from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    KinesisVideoError as KinesisVideoError,
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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .account_channel_limit_exceeded_exception import (
    AccountChannelLimitExceededException as AccountChannelLimitExceededException,
)
from .account_stream_limit_exceeded_exception import (
    AccountStreamLimitExceededException as AccountStreamLimitExceededException,
)
from .client_limit_exceeded_exception import (
    ClientLimitExceededException as ClientLimitExceededException,
)
from .device_stream_limit_exceeded_exception import (
    DeviceStreamLimitExceededException as DeviceStreamLimitExceededException,
)
from .invalid_argument_exception import (
    InvalidArgumentException as InvalidArgumentException,
)
from .invalid_device_exception import InvalidDeviceException as InvalidDeviceException
from .invalid_resource_format_exception import (
    InvalidResourceFormatException as InvalidResourceFormatException,
)
from .no_data_retention_exception import (
    NoDataRetentionException as NoDataRetentionException,
)
from .not_authorized_exception import NotAuthorizedException as NotAuthorizedException
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .stream_edge_configuration_not_found_exception import (
    StreamEdgeConfigurationNotFoundException as StreamEdgeConfigurationNotFoundException,
)
from .tags_per_resource_exceeded_limit_exception import (
    TagsPerResourceExceededLimitException as TagsPerResourceExceededLimitException,
)
from .version_mismatch_exception import (
    VersionMismatchException as VersionMismatchException,
)
