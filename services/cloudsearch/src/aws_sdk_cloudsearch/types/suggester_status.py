"""Generated from Smithy shape ``com.amazonaws.cloudsearch#SuggesterStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.option_status
    import aws_sdk_cloudsearch.types.suggester


class SuggesterStatus(TypedDict, closed=True):
    options: "aws_sdk_cloudsearch.types.suggester.Suggester"
    status: "aws_sdk_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: SuggesterStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.suggester

    aws_sdk_cloudsearch.types.suggester.serialize_query(
        value["options"], pairs, f"{prefix}.Options"
    )
    import aws_sdk_cloudsearch.types.option_status

    aws_sdk_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> SuggesterStatus:
    out: SuggesterStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_cloudsearch.types.suggester

        out["options"] = aws_sdk_cloudsearch.types.suggester.deserialize_query(
            child_options
        )
    else:
        raise DeserializationError("SuggesterStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudsearch.types.option_status

        out["status"] = aws_sdk_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("SuggesterStatus.status required")
    return out
