"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetViewInput``."""

from typing_extensions import TypedDict

from capo_resource_explorer_2.errors import DeserializationError


class GetViewInput(TypedDict, closed=True):
    view_arn: "str"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetViewInput) -> dict:
    out: dict = {}
    out["ViewArn"] = value["view_arn"]
    return out


def deserialize_json(data: dict) -> GetViewInput:
    out: GetViewInput = {}  # type: ignore[typeddict-item]
    if "ViewArn" in data:
        out["view_arn"] = data["ViewArn"]
    else:
        raise DeserializationError("GetViewInput.view_arn required")
    return out
