"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEksClusterLoggingClusterLoggingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string_list


class AwsEksClusterLoggingClusterLoggingDetails(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the logging types that are listed in <code>Types</code> are enabled.</p>"""
    types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of logging types. Valid values are as follows:</p> <ul> <li> <p> <code>api</code> </p> </li> <li> <p> <code>audit</code> </p> </li> <li> <p> <code>authenticator</code> </p> </li> <li> <p> <code>controllerManager</code> </p> </li> <li> <p> <code>scheduler</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksClusterLoggingClusterLoggingDetails) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Types"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["types"]
        )
    return out


def deserialize_json(data: dict) -> AwsEksClusterLoggingClusterLoggingDetails:
    out: AwsEksClusterLoggingClusterLoggingDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Types" in data:
        import capo_securityhub.types.non_empty_string_list

        out["types"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Types"]
        )
    return out
