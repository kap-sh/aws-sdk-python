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
    SSOOIDCError as SSOOIDCError,
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
from .authorization_pending_exception import (
    AuthorizationPendingException as AuthorizationPendingException,
)
from .expired_token_exception import ExpiredTokenException as ExpiredTokenException
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_client_exception import InvalidClientException as InvalidClientException
from .invalid_client_metadata_exception import (
    InvalidClientMetadataException as InvalidClientMetadataException,
)
from .invalid_grant_exception import InvalidGrantException as InvalidGrantException
from .invalid_redirect_uri_exception import (
    InvalidRedirectUriException as InvalidRedirectUriException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_request_region_exception import (
    InvalidRequestRegionException as InvalidRequestRegionException,
)
from .invalid_scope_exception import InvalidScopeException as InvalidScopeException
from .slow_down_exception import SlowDownException as SlowDownException
from .unauthorized_client_exception import (
    UnauthorizedClientException as UnauthorizedClientException,
)
from .unsupported_grant_type_exception import (
    UnsupportedGrantTypeException as UnsupportedGrantTypeException,
)
