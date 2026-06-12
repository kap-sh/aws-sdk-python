"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalEnis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.efa_enis


class AdditionalEnis(TypedDict):
    efa_enis: NotRequired["aws_sdk_sagemaker.types.efa_enis.EfaEnis"]
    """<p>A list of Elastic Fabric Adapter (EFA) ENIs associated with the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalEnis) -> dict:
    out: dict = {}
    if "efa_enis" in value:
        import aws_sdk_sagemaker.types.efa_enis

        out["EfaEnis"] = aws_sdk_sagemaker.types.efa_enis.serialize_aws_json_1_1(
            value["efa_enis"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalEnis:
    out: AdditionalEnis = {}  # type: ignore[typeddict-item]
    if "EfaEnis" in data:
        import aws_sdk_sagemaker.types.efa_enis

        out["efa_enis"] = aws_sdk_sagemaker.types.efa_enis.deserialize_aws_json_1_1(
            data["EfaEnis"]
        )
    return out
