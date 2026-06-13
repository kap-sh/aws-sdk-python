"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#DeleteIndexInput``."""

from typing import TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError


class DeleteIndexInput(TypedDict):
    arn: "str"
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the index that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIndexInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteIndexInput:
    out: DeleteIndexInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeleteIndexInput.arn required")
    return out
