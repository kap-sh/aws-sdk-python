"""Generated from Smithy shape ``com.amazonaws.rds#DeleteOptionGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DeleteOptionGroupMessage(TypedDict, closed=True):
    option_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the option group to be deleted.</p> <note> <p>You can't delete default option groups.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteOptionGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_group_name" in value:
        pairs.append((f"{prefix}.OptionGroupName", str(value["option_group_name"])))


def deserialize_query(el: Element) -> DeleteOptionGroupMessage:
    out: DeleteOptionGroupMessage = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    return out
