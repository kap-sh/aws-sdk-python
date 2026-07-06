"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.group_identifier
    import aws_sdk_application_signals.types.group_name
    import aws_sdk_application_signals.types.group_source
    import aws_sdk_application_signals.types.group_value


class ServiceGroup(TypedDict, closed=True):
    group_name: "aws_sdk_application_signals.types.group_name.GroupName"
    """<p>The name of the grouping attribute, such as <code>BusinessUnit</code> or <code>Environment</code>.</p>"""
    group_value: "aws_sdk_application_signals.types.group_value.GroupValue"
    """<p>The value of the grouping attribute for this service, such as <code>Payments</code> or <code>Production</code>.</p>"""
    group_source: "aws_sdk_application_signals.types.group_source.GroupSource"
    """<p>The source of the grouping attribute, such as <code>TAG</code>, <code>OTEL</code>, or <code>DEFAULT</code>.</p>"""
    group_identifier: (
        "aws_sdk_application_signals.types.group_identifier.GroupIdentifier"
    )
    """<p>A unique identifier for this grouping attribute value, used for filtering and API operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceGroup) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["GroupValue"] = value["group_value"]
    out["GroupSource"] = value["group_source"]
    out["GroupIdentifier"] = value["group_identifier"]
    return out


def deserialize_json(data: dict) -> ServiceGroup:
    out: ServiceGroup = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    else:
        raise DeserializationError("ServiceGroup.group_name required")
    if "GroupValue" in data:
        out["group_value"] = data["GroupValue"]
    else:
        raise DeserializationError("ServiceGroup.group_value required")
    if "GroupSource" in data:
        out["group_source"] = data["GroupSource"]
    else:
        raise DeserializationError("ServiceGroup.group_source required")
    if "GroupIdentifier" in data:
        out["group_identifier"] = data["GroupIdentifier"]
    else:
        raise DeserializationError("ServiceGroup.group_identifier required")
    return out
