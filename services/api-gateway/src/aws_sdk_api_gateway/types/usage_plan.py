"""Generated from Smithy shape ``com.amazonaws.apigateway#UsagePlan``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_api_stage
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.quota_settings
    import aws_sdk_api_gateway.types.string
    import aws_sdk_api_gateway.types.throttle_settings


class UsagePlan(TypedDict):
    id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The identifier of a UsagePlan resource.</p>"""
    name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of a usage plan.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of a usage plan.</p>"""
    api_stages: NotRequired[
        "aws_sdk_api_gateway.types.list_of_api_stage.ListOfApiStage"
    ]
    """<p>The associated API stages of a usage plan.</p>"""
    throttle: NotRequired[
        "aws_sdk_api_gateway.types.throttle_settings.ThrottleSettings"
    ]
    """<p>A map containing method level throttling information for API stage in a usage plan.</p>"""
    quota: NotRequired["aws_sdk_api_gateway.types.quota_settings.QuotaSettings"]
    """<p>The target maximum number of permitted requests per a given unit time interval.</p>"""
    product_code: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The Amazon Web Services Marketplace product identifier to associate with the usage plan as a SaaS product on the Amazon Web Services Marketplace.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsagePlan) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "api_stages" in value:
        import aws_sdk_api_gateway.types.list_of_api_stage

        out["apiStages"] = aws_sdk_api_gateway.types.list_of_api_stage.serialize_json(
            value["api_stages"]
        )
    if "throttle" in value:
        import aws_sdk_api_gateway.types.throttle_settings

        out["throttle"] = aws_sdk_api_gateway.types.throttle_settings.serialize_json(
            value["throttle"]
        )
    if "quota" in value:
        import aws_sdk_api_gateway.types.quota_settings

        out["quota"] = aws_sdk_api_gateway.types.quota_settings.serialize_json(
            value["quota"]
        )
    if "product_code" in value:
        out["productCode"] = value["product_code"]
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UsagePlan:
    out: UsagePlan = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "apiStages" in data:
        import aws_sdk_api_gateway.types.list_of_api_stage

        out["api_stages"] = (
            aws_sdk_api_gateway.types.list_of_api_stage.deserialize_json(
                data["apiStages"]
            )
        )
    if "throttle" in data:
        import aws_sdk_api_gateway.types.throttle_settings

        out["throttle"] = aws_sdk_api_gateway.types.throttle_settings.deserialize_json(
            data["throttle"]
        )
    if "quota" in data:
        import aws_sdk_api_gateway.types.quota_settings

        out["quota"] = aws_sdk_api_gateway.types.quota_settings.deserialize_json(
            data["quota"]
        )
    if "productCode" in data:
        out["product_code"] = data["productCode"]
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
