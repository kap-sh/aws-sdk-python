"""Generated from Smithy shape ``com.amazonaws.appintegrations#IframeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.iframe_permission_list


class IframeConfig(TypedDict, closed=True):
    allow: NotRequired[
        "aws_sdk_appintegrations.types.iframe_permission_list.IframePermissionList"
    ]
    """<p>The list of features that are allowed in the iframe.</p>"""
    sandbox: NotRequired[
        "aws_sdk_appintegrations.types.iframe_permission_list.IframePermissionList"
    ]
    """<p>The list of sandbox attributes for the iframe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IframeConfig) -> dict:
    out: dict = {}
    if "allow" in value:
        import aws_sdk_appintegrations.types.iframe_permission_list

        out["Allow"] = (
            aws_sdk_appintegrations.types.iframe_permission_list.serialize_json(
                value["allow"]
            )
        )
    if "sandbox" in value:
        import aws_sdk_appintegrations.types.iframe_permission_list

        out["Sandbox"] = (
            aws_sdk_appintegrations.types.iframe_permission_list.serialize_json(
                value["sandbox"]
            )
        )
    return out


def deserialize_json(data: dict) -> IframeConfig:
    out: IframeConfig = {}  # type: ignore[typeddict-item]
    if "Allow" in data:
        import aws_sdk_appintegrations.types.iframe_permission_list

        out["allow"] = (
            aws_sdk_appintegrations.types.iframe_permission_list.deserialize_json(
                data["Allow"]
            )
        )
    if "Sandbox" in data:
        import aws_sdk_appintegrations.types.iframe_permission_list

        out["sandbox"] = (
            aws_sdk_appintegrations.types.iframe_permission_list.deserialize_json(
                data["Sandbox"]
            )
        )
    return out
