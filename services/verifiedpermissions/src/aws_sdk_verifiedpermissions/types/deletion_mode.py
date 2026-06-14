"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

"""<p>The deletion mode for a resource. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The resource enters the <code>PendingDeletion</code> state. This is the default behavior.</p> </li> <li> <p> <b>HardDelete</b> – The resource is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>"""
DeletionMode: TypeAlias = Literal[
    "SoftDelete",
    "HardDelete",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SoftDelete",
        "HardDelete",
    )
)


def serialize_aws_json_1_0(value: DeletionMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeletionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletionMode value: {data!r}")
    return cast(DeletionMode, data)
