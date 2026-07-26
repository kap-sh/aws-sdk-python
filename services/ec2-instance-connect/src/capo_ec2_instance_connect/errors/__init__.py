from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    EC2InstanceConnectError as EC2InstanceConnectError,
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
from .auth_exception import AuthException as AuthException
from .ec2_instance_not_found_exception import (
    EC2InstanceNotFoundException as EC2InstanceNotFoundException,
)
from .ec2_instance_state_invalid_exception import (
    EC2InstanceStateInvalidException as EC2InstanceStateInvalidException,
)
from .ec2_instance_type_invalid_exception import (
    EC2InstanceTypeInvalidException as EC2InstanceTypeInvalidException,
)
from .ec2_instance_unavailable_exception import (
    EC2InstanceUnavailableException as EC2InstanceUnavailableException,
)
from .invalid_args_exception import InvalidArgsException as InvalidArgsException
from .serial_console_access_disabled_exception import (
    SerialConsoleAccessDisabledException as SerialConsoleAccessDisabledException,
)
from .serial_console_session_limit_exceeded_exception import (
    SerialConsoleSessionLimitExceededException as SerialConsoleSessionLimitExceededException,
)
from .serial_console_session_unavailable_exception import (
    SerialConsoleSessionUnavailableException as SerialConsoleSessionUnavailableException,
)
from .serial_console_session_unsupported_exception import (
    SerialConsoleSessionUnsupportedException as SerialConsoleSessionUnsupportedException,
)
from .service_exception import ServiceException as ServiceException
from .throttling_exception import ThrottlingException as ThrottlingException
