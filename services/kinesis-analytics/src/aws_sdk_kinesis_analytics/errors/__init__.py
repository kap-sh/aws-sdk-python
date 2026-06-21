from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    KinesisAnalyticsError as KinesisAnalyticsError,
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
from .code_validation_exception import (
    CodeValidationException as CodeValidationException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .invalid_application_configuration_exception import (
    InvalidApplicationConfigurationException as InvalidApplicationConfigurationException,
)
from .invalid_argument_exception import (
    InvalidArgumentException as InvalidArgumentException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_provisioned_throughput_exceeded_exception import (
    ResourceProvisionedThroughputExceededException as ResourceProvisionedThroughputExceededException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unable_to_detect_schema_exception import (
    UnableToDetectSchemaException as UnableToDetectSchemaException,
)
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)
