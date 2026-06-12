"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourcePath``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.resource_path_component_list


class ResourcePath(TypedDict):
    components: NotRequired[
        "aws_sdk_workdocs.types.resource_path_component_list.ResourcePathComponentList"
    ]
    """<p>The components of the resource path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePath) -> dict:
    out: dict = {}
    if "components" in value:
        import aws_sdk_workdocs.types.resource_path_component_list

        out["Components"] = (
            aws_sdk_workdocs.types.resource_path_component_list.serialize_json(
                value["components"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcePath:
    out: ResourcePath = {}  # type: ignore[typeddict-item]
    if "Components" in data:
        import aws_sdk_workdocs.types.resource_path_component_list

        out["components"] = (
            aws_sdk_workdocs.types.resource_path_component_list.deserialize_json(
                data["Components"]
            )
        )
    return out
