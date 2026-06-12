"""Generated from Smithy shape ``com.amazonaws.cloudsearch#IndexFieldStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.index_field
    import aws_sdk_cloudsearch.types.option_status


class IndexFieldStatus(TypedDict):
    options: "aws_sdk_cloudsearch.types.index_field.IndexField"
    status: "aws_sdk_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: IndexFieldStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.index_field

    aws_sdk_cloudsearch.types.index_field.serialize_query(
        value["options"], pairs, f"{prefix}.Options"
    )
    import aws_sdk_cloudsearch.types.option_status

    aws_sdk_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> IndexFieldStatus:
    out: IndexFieldStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_cloudsearch.types.index_field

        out["options"] = aws_sdk_cloudsearch.types.index_field.deserialize_query(
            child_options
        )
    else:
        raise DeserializationError("IndexFieldStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudsearch.types.option_status

        out["status"] = aws_sdk_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("IndexFieldStatus.status required")
    return out
