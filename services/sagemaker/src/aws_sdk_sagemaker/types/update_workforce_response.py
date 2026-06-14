"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateWorkforceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workforce


class UpdateWorkforceResponse(TypedDict):
    workforce: NotRequired["aws_sdk_sagemaker.types.workforce.Workforce"]
    r"""<p>A single private workforce. You can create one private work force in each Amazon Web Services Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html\">Create a Private Workforce</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkforceResponse) -> dict:
    out: dict = {}
    if "workforce" in value:
        import aws_sdk_sagemaker.types.workforce

        out["Workforce"] = aws_sdk_sagemaker.types.workforce.serialize_aws_json_1_1(
            value["workforce"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkforceResponse:
    out: UpdateWorkforceResponse = {}  # type: ignore[typeddict-item]
    if "Workforce" in data:
        import aws_sdk_sagemaker.types.workforce

        out["workforce"] = aws_sdk_sagemaker.types.workforce.deserialize_aws_json_1_1(
            data["Workforce"]
        )
    return out
