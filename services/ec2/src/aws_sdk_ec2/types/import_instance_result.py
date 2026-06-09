"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task


class ImportInstanceResult(TypedDict):
    conversion_task: NotRequired["aws_sdk_ec2.types.conversion_task.ConversionTask"]
    """<p>Information about the conversion task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "conversion_task" in value:
        import aws_sdk_ec2.types.conversion_task

        aws_sdk_ec2.types.conversion_task.serialize_ec2_query(
            value["conversion_task"], pairs, f"{prefix}.ConversionTask"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceResult:
    out: ImportInstanceResult = {}  # type: ignore[typeddict-item]
    child_conversion_task = el.find("ConversionTask")
    if child_conversion_task is not None:
        import aws_sdk_ec2.types.conversion_task

        out["conversion_task"] = (
            aws_sdk_ec2.types.conversion_task.deserialize_ec2_query(
                child_conversion_task
            )
        )
    return out
