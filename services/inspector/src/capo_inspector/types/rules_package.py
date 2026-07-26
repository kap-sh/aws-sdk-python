"""Generated from Smithy shape ``com.amazonaws.inspector#RulesPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.provider_name
    import capo_inspector.types.rules_package_name
    import capo_inspector.types.text
    import capo_inspector.types.version


class RulesPackage(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the rules package.</p>"""
    name: "capo_inspector.types.rules_package_name.RulesPackageName"
    """<p>The name of the rules package.</p>"""
    version: "capo_inspector.types.version.Version"
    """<p>The version ID of the rules package.</p>"""
    provider: "capo_inspector.types.provider_name.ProviderName"
    """<p>The provider of the rules package.</p>"""
    description: NotRequired["capo_inspector.types.text.Text"]
    """<p>The description of the rules package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RulesPackage) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    out["provider"] = value["provider"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RulesPackage:
    out: RulesPackage = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RulesPackage.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RulesPackage.name required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("RulesPackage.version required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RulesPackage.provider required")
    if "description" in data:
        out["description"] = data["description"]
    return out
