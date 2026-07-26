"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionRunAsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__integer


class FunctionRunAsConfig(TypedDict, closed=True):
    gid: NotRequired["capo_greengrass.types.__integer.__integer"]
    """The group ID whose permissions are used to run a Lambda function."""
    uid: NotRequired["capo_greengrass.types.__integer.__integer"]
    """The user ID whose permissions are used to run a Lambda function."""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionRunAsConfig) -> dict:
    out: dict = {}
    if "gid" in value:
        out["Gid"] = value["gid"]
    if "uid" in value:
        out["Uid"] = value["uid"]
    return out


def deserialize_json(data: dict) -> FunctionRunAsConfig:
    out: FunctionRunAsConfig = {}  # type: ignore[typeddict-item]
    if "Gid" in data:
        out["gid"] = data["Gid"]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    return out
