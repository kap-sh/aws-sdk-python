"""Generated from Smithy shape ``com.amazonaws.eks#LogSetup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean
    import aws_sdk_eks.types.log_types


class LogSetup(TypedDict, closed=True):
    types: NotRequired["aws_sdk_eks.types.log_types.LogTypes"]
    """<p>The available cluster control plane log types.</p>"""
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs . If a log type isn't enabled, that log type doesn't export its control plane logs. Each individual log type can be enabled or disabled independently.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogSetup) -> dict:
    out: dict = {}
    if "types" in value:
        import aws_sdk_eks.types.log_types

        out["types"] = aws_sdk_eks.types.log_types.serialize_json(value["types"])
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> LogSetup:
    out: LogSetup = {}  # type: ignore[typeddict-item]
    if "types" in data:
        import aws_sdk_eks.types.log_types

        out["types"] = aws_sdk_eks.types.log_types.deserialize_json(data["types"])
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
