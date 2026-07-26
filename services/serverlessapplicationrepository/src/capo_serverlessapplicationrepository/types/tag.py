"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    r"""<p>This property corresponds to the content of the same name for the <i>AWS CloudFormation <a href=\"https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag\">Tag</a> </i> Data Type.</p>"""
    value: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    r"""<p>This property corresponds to the content of the same name for the <i>AWS CloudFormation <a href=\"https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag\"> Tag</a> </i> Data Type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
