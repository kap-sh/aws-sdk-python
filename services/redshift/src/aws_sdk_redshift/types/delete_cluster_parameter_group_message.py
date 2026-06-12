"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DeleteClusterParameterGroupMessage(TypedDict):
    parameter_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the parameter group to be deleted.</p> <p>Constraints:</p> <ul> <li> <p>Must be the name of an existing cluster parameter group.</p> </li> <li> <p>Cannot delete a default cluster parameter group.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupName", str(value["parameter_group_name"]))
        )


def deserialize_query(el: Element) -> DeleteClusterParameterGroupMessage:
    out: DeleteClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    return out
