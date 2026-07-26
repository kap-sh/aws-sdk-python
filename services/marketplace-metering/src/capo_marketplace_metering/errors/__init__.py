from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    MarketplaceMeteringError as MarketplaceMeteringError,
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
from .customer_not_entitled_exception import (
    CustomerNotEntitledException as CustomerNotEntitledException,
)
from .disabled_api_exception import DisabledApiException as DisabledApiException
from .duplicate_request_exception import (
    DuplicateRequestException as DuplicateRequestException,
)
from .expired_token_exception import ExpiredTokenException as ExpiredTokenException
from .idempotency_conflict_exception import (
    IdempotencyConflictException as IdempotencyConflictException,
)
from .internal_service_error_exception import (
    InternalServiceErrorException as InternalServiceErrorException,
)
from .invalid_customer_identifier_exception import (
    InvalidCustomerIdentifierException as InvalidCustomerIdentifierException,
)
from .invalid_endpoint_region_exception import (
    InvalidEndpointRegionException as InvalidEndpointRegionException,
)
from .invalid_license_exception import (
    InvalidLicenseException as InvalidLicenseException,
)
from .invalid_product_code_exception import (
    InvalidProductCodeException as InvalidProductCodeException,
)
from .invalid_public_key_version_exception import (
    InvalidPublicKeyVersionException as InvalidPublicKeyVersionException,
)
from .invalid_region_exception import InvalidRegionException as InvalidRegionException
from .invalid_tag_exception import InvalidTagException as InvalidTagException
from .invalid_token_exception import InvalidTokenException as InvalidTokenException
from .invalid_usage_allocations_exception import (
    InvalidUsageAllocationsException as InvalidUsageAllocationsException,
)
from .invalid_usage_dimension_exception import (
    InvalidUsageDimensionException as InvalidUsageDimensionException,
)
from .platform_not_supported_exception import (
    PlatformNotSupportedException as PlatformNotSupportedException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .timestamp_out_of_bounds_exception import (
    TimestampOutOfBoundsException as TimestampOutOfBoundsException,
)
