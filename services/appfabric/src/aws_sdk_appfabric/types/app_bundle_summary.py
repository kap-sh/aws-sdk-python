"""Generated from Smithy shape ``com.amazonaws.appfabric#AppBundleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.arn


class AppBundleSummary(TypedDict):
    arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app bundle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppBundleSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AppBundleSummary:
    out: AppBundleSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AppBundleSummary.arn required")
    return out
