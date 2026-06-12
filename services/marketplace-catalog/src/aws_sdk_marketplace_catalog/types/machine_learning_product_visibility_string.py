"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

"""<p>The visibility status of a machine learning product. Valid values are:</p> <ul> <li> <p> <code>Limited</code> - The product is available to a limited set of buyers.</p> </li> <li> <p> <code>Public</code> - The product is publicly available to all buyers.</p> </li> <li> <p> <code>Restricted</code> - The product has restricted availability.</p> </li> <li> <p> <code>Draft</code> - The product is in draft state and not yet available to buyers.</p> </li> </ul>"""
MachineLearningProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Draft",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Limited",
        "Public",
        "Restricted",
        "Draft",
    )
)


def serialize_json(value: MachineLearningProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> MachineLearningProductVisibilityString:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MachineLearningProductVisibilityString value: {data!r}"
        )
    return cast(MachineLearningProductVisibilityString, data)
