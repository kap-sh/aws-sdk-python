"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateDistributionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.distribution_list
    import capo_imagebuilder.types.non_empty_string


class UpdateDistributionConfigurationRequest(TypedDict, closed=True):
    distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that you want to update.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the distribution configuration.</p>"""
    distributions: "capo_imagebuilder.types.distribution_list.DistributionList"
    """<p>The distributions of the distribution configuration.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDistributionConfigurationRequest) -> dict:
    out: dict = {}
    out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_imagebuilder.types.distribution_list

    out["distributions"] = capo_imagebuilder.types.distribution_list.serialize_json(
        value["distributions"]
    )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDistributionConfigurationRequest:
    out: UpdateDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "distributionConfigurationArn" in data:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateDistributionConfigurationRequest.distribution_configuration_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "distributions" in data:
        import capo_imagebuilder.types.distribution_list

        out["distributions"] = (
            capo_imagebuilder.types.distribution_list.deserialize_json(
                data["distributions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDistributionConfigurationRequest.distributions required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "UpdateDistributionConfigurationRequest.client_token required"
        )
    return out
