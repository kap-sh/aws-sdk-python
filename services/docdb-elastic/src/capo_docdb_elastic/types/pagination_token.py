"""Generated from Smithy shape ``com.amazonaws.docdbelastic#PaginationToken``."""

from typing import TypeAlias

"""Token or cursor used in paginated operations. When this value is provided as operation input, the service returns results from where the previous response left off. When this value is present in operation output, it indicates that there are more results to retrieve. This should be opaque to not expose implementation details and potentially versioned to allow evolution of pagination strategy."""
PaginationToken: TypeAlias = str
