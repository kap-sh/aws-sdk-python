"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupOptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_group_options_list
    import aws_sdk_rds.types.string


class OptionGroupOptionsMessage(TypedDict, closed=True):
    option_group_options: NotRequired[
        "aws_sdk_rds.types.option_group_options_list.OptionGroupOptionsList"
    ]
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupOptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_group_options" in value:
        import aws_sdk_rds.types.option_group_options_list

        aws_sdk_rds.types.option_group_options_list.serialize_query(
            value["option_group_options"], pairs, f"{prefix}.OptionGroupOptions"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> OptionGroupOptionsMessage:
    out: OptionGroupOptionsMessage = {}  # type: ignore[typeddict-item]
    child_option_group_options = el.find("OptionGroupOptions")
    if child_option_group_options is not None:
        import aws_sdk_rds.types.option_group_options_list

        out["option_group_options"] = (
            aws_sdk_rds.types.option_group_options_list.deserialize_query(
                child_option_group_options
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
