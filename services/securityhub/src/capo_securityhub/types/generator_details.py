"""Generated from Smithy shape ``com.amazonaws.securityhub#GeneratorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.type_list


class GeneratorDetails(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the detector used to identify the code vulnerability. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The description of the detector used to identify the code vulnerability. </p>"""
    labels: NotRequired["capo_securityhub.types.type_list.TypeList"]
    """<p> An array of tags used to identify the detector associated with the finding. </p> <p>Array Members: Minimum number of 0 items. Maximum number of 10 items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratorDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "labels" in value:
        import capo_securityhub.types.type_list

        out["Labels"] = capo_securityhub.types.type_list.serialize_json(value["labels"])
    return out


def deserialize_json(data: dict) -> GeneratorDetails:
    out: GeneratorDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Labels" in data:
        import capo_securityhub.types.type_list

        out["labels"] = capo_securityhub.types.type_list.deserialize_json(
            data["Labels"]
        )
    return out
