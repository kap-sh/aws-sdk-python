"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedPermissionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.timestamp
    import aws_sdk_accessanalyzer.types.unused_action_list


class UnusedPermissionDetails(TypedDict):
    actions: NotRequired[
        "aws_sdk_accessanalyzer.types.unused_action_list.UnusedActionList"
    ]
    """<p>A list of unused actions for which the unused access finding was generated.</p>"""
    service_namespace: "str"
    """<p>The namespace of the Amazon Web Services service that contains the unused actions.</p>"""
    last_accessed: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the permission was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedPermissionDetails) -> dict:
    out: dict = {}
    if "actions" in value:
        import aws_sdk_accessanalyzer.types.unused_action_list

        out["actions"] = aws_sdk_accessanalyzer.types.unused_action_list.serialize_json(
            value["actions"]
        )
    out["serviceNamespace"] = value["service_namespace"]
    if "last_accessed" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["lastAccessed"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedPermissionDetails:
    out: UnusedPermissionDetails = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import aws_sdk_accessanalyzer.types.unused_action_list

        out["actions"] = (
            aws_sdk_accessanalyzer.types.unused_action_list.deserialize_json(
                data["actions"]
            )
        )
    if "serviceNamespace" in data:
        out["service_namespace"] = data["serviceNamespace"]
    else:
        raise DeserializationError("UnusedPermissionDetails.service_namespace required")
    if "lastAccessed" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["last_accessed"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
