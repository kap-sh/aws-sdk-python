"""Generated from Smithy shape ``com.amazonaws.codecatalyst#IdeConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class IdeConfiguration(TypedDict, closed=True):
    runtime: NotRequired["str"]
    """<p>A link to the IDE runtime image. </p> <note> <p>This parameter is not required for <code>VSCode</code>.</p> </note>"""
    name: NotRequired["str"]
    """<p>The name of the IDE. Valid values include <code>Cloud9</code>, <code>IntelliJ</code>, <code>PyCharm</code>, <code>GoLand</code>, and <code>VSCode</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdeConfiguration) -> dict:
    out: dict = {}
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IdeConfiguration:
    out: IdeConfiguration = {}  # type: ignore[typeddict-item]
    if "runtime" in data:
        out["runtime"] = data["runtime"]
    if "name" in data:
        out["name"] = data["name"]
    return out
