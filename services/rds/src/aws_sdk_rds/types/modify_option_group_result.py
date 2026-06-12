"""Generated from Smithy shape ``com.amazonaws.rds#ModifyOptionGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_group


class ModifyOptionGroupResult(TypedDict):
    option_group: NotRequired["aws_sdk_rds.types.option_group.OptionGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyOptionGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_group" in value:
        import aws_sdk_rds.types.option_group

        aws_sdk_rds.types.option_group.serialize_query(
            value["option_group"], pairs, f"{prefix}.OptionGroup"
        )


def deserialize_query(el: Element) -> ModifyOptionGroupResult:
    out: ModifyOptionGroupResult = {}  # type: ignore[typeddict-item]
    child_option_group = el.find("OptionGroup")
    if child_option_group is not None:
        import aws_sdk_rds.types.option_group

        out["option_group"] = aws_sdk_rds.types.option_group.deserialize_query(
            child_option_group
        )
    return out
