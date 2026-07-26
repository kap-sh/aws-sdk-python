"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkloadSpec``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.string


class _WorkloadSpec_Inline(TypedDict, closed=True):
    Inline: "capo_sagemaker.types.string.String"


WorkloadSpec: TypeAlias = _WorkloadSpec_Inline


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkloadSpec) -> dict:
    if "Inline" in value:
        return {"Inline": value["Inline"]}
    else:
        raise SerializationError("WorkloadSpec: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WorkloadSpec:
    if "Inline" in data:
        return {"Inline": data["Inline"]}
    else:
        raise DeserializationError("WorkloadSpec: no recognized variant key")
