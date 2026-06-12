"""Generated from Smithy shape ``com.amazonaws.acmpca#Qualifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.string256


class Qualifier(TypedDict):
    cps_uri: "aws_sdk_acm_pca.types.string256.String256"
    """<p>Contains a pointer to a certification practice statement (CPS) published by the CA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Qualifier) -> dict:
    out: dict = {}
    out["CpsUri"] = value["cps_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Qualifier:
    out: Qualifier = {}  # type: ignore[typeddict-item]
    if "CpsUri" in data:
        out["cps_uri"] = data["CpsUri"]
    else:
        raise DeserializationError("Qualifier.cps_uri required")
    return out
