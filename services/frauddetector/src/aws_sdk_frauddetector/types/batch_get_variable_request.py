"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchGetVariableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.name_list


class BatchGetVariableRequest(TypedDict, closed=True):
    names: "aws_sdk_frauddetector.types.name_list.NameList"
    """<p>The list of variable names to get.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetVariableRequest) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.name_list

    out["names"] = aws_sdk_frauddetector.types.name_list.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetVariableRequest:
    out: BatchGetVariableRequest = {}  # type: ignore[typeddict-item]
    if "names" in data:
        import aws_sdk_frauddetector.types.name_list

        out["names"] = aws_sdk_frauddetector.types.name_list.deserialize_aws_json_1_1(
            data["names"]
        )
    else:
        raise DeserializationError("BatchGetVariableRequest.names required")
    return out
