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
    TranslateError as TranslateError,
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
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflict_exception import ConflictException as ConflictException
from .detected_language_low_confidence_exception import (
    DetectedLanguageLowConfidenceException as DetectedLanguageLowConfidenceException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_filter_exception import InvalidFilterException as InvalidFilterException
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .text_size_limit_exceeded_exception import (
    TextSizeLimitExceededException as TextSizeLimitExceededException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unsupported_display_language_code_exception import (
    UnsupportedDisplayLanguageCodeException as UnsupportedDisplayLanguageCodeException,
)
from .unsupported_language_pair_exception import (
    UnsupportedLanguagePairException as UnsupportedLanguagePairException,
)
