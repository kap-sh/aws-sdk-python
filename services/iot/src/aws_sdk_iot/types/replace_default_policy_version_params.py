"""Generated from Smithy shape ``com.amazonaws.iot#ReplaceDefaultPolicyVersionParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_template_name


class ReplaceDefaultPolicyVersionParams(TypedDict, closed=True):
    template_name: "aws_sdk_iot.types.policy_template_name.PolicyTemplateName"
    """<p>The name of the template to be applied. The only supported value is <code>BLANK_POLICY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplaceDefaultPolicyVersionParams) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.policy_template_name

    out["templateName"] = aws_sdk_iot.types.policy_template_name.serialize_json(
        value["template_name"]
    )
    return out


def deserialize_json(data: dict) -> ReplaceDefaultPolicyVersionParams:
    out: ReplaceDefaultPolicyVersionParams = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        import aws_sdk_iot.types.policy_template_name

        out["template_name"] = aws_sdk_iot.types.policy_template_name.deserialize_json(
            data["templateName"]
        )
    else:
        raise DeserializationError(
            "ReplaceDefaultPolicyVersionParams.template_name required"
        )
    return out
