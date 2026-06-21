from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    DirectConnectError as DirectConnectError,
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
from .direct_connect_client_exception import (
    DirectConnectClientException as DirectConnectClientException,
)
from .direct_connect_server_exception import (
    DirectConnectServerException as DirectConnectServerException,
)
from .duplicate_tag_keys_exception import (
    DuplicateTagKeysException as DuplicateTagKeysException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
