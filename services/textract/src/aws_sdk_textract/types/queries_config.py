"""Generated from Smithy shape ``com.amazonaws.textract#QueriesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.queries


class QueriesConfig(TypedDict, closed=True):
    queries: "aws_sdk_textract.types.queries.Queries"
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueriesConfig) -> dict:
    out: dict = {}
    import aws_sdk_textract.types.queries

    out["Queries"] = aws_sdk_textract.types.queries.serialize_aws_json_1_1(
        value["queries"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueriesConfig:
    out: QueriesConfig = {}  # type: ignore[typeddict-item]
    if "Queries" in data:
        import aws_sdk_textract.types.queries

        out["queries"] = aws_sdk_textract.types.queries.deserialize_aws_json_1_1(
            data["Queries"]
        )
    else:
        raise DeserializationError("QueriesConfig.queries required")
    return out
