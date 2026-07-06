"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.action_order
    import aws_sdk_elastic_load_balancing_v2.types.action_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_config
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_config
    import aws_sdk_elastic_load_balancing_v2.types.fixed_response_action_config
    import aws_sdk_elastic_load_balancing_v2.types.forward_action_config
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_config
    import aws_sdk_elastic_load_balancing_v2.types.redirect_action_config
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn


class Action(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.action_type_enum.ActionTypeEnum"
    ]
    """<p>The type of action.</p>"""
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group. Specify only when <code>Type</code> is <code>forward</code> and you want to route to a single target group. To route to multiple target groups, you must use <code>ForwardConfig</code> instead.</p>"""
    authenticate_oidc_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_config.AuthenticateOidcActionConfig"
    ]
    """<p>[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when <code>Type</code> is <code>authenticate-oidc</code>.</p>"""
    authenticate_cognito_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_config.AuthenticateCognitoActionConfig"
    ]
    """<p>[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when <code>Type</code> is <code>authenticate-cognito</code>.</p>"""
    order: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.action_order.ActionOrder"
    ]
    """<p>The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.</p>"""
    redirect_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.redirect_action_config.RedirectActionConfig"
    ]
    """<p>[Application Load Balancer] Information for creating a redirect action. Specify only when <code>Type</code> is <code>redirect</code>.</p>"""
    fixed_response_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.fixed_response_action_config.FixedResponseActionConfig"
    ]
    """<p>[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when <code>Type</code> is <code>fixed-response</code>.</p>"""
    forward_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.forward_action_config.ForwardActionConfig"
    ]
    """<p>Information for creating an action that distributes requests among multiple target groups. Specify only when <code>Type</code> is <code>forward</code>.</p> <p>If you specify both <code>ForwardConfig</code> and <code>TargetGroupArn</code>, you can specify only one target group using <code>ForwardConfig</code> and it must be the same target group specified in <code>TargetGroupArn</code>.</p>"""
    jwt_validation_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_config.JwtValidationActionConfig"
    ]
    """<p>[HTTPS listeners] Information for validating JWT access tokens in client requests. Specify only when <code>Type</code> is <code>jwt-validation</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Action, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.action_type_enum

        aws_sdk_elastic_load_balancing_v2.types.action_type_enum.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "authenticate_oidc_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_config

        aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_config.serialize_query(
            value["authenticate_oidc_config"], pairs, f"{prefix}.AuthenticateOidcConfig"
        )
    if "authenticate_cognito_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_config

        aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_config.serialize_query(
            value["authenticate_cognito_config"],
            pairs,
            f"{prefix}.AuthenticateCognitoConfig",
        )
    if "order" in value:
        pairs.append((f"{prefix}.Order", str(value["order"])))
    if "redirect_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.redirect_action_config

        aws_sdk_elastic_load_balancing_v2.types.redirect_action_config.serialize_query(
            value["redirect_config"], pairs, f"{prefix}.RedirectConfig"
        )
    if "fixed_response_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.fixed_response_action_config

        aws_sdk_elastic_load_balancing_v2.types.fixed_response_action_config.serialize_query(
            value["fixed_response_config"], pairs, f"{prefix}.FixedResponseConfig"
        )
    if "forward_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.forward_action_config

        aws_sdk_elastic_load_balancing_v2.types.forward_action_config.serialize_query(
            value["forward_config"], pairs, f"{prefix}.ForwardConfig"
        )
    if "jwt_validation_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_config

        aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_config.serialize_query(
            value["jwt_validation_config"], pairs, f"{prefix}.JwtValidationConfig"
        )


def deserialize_query(el: Element) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.action_type_enum

        out["type"] = (
            aws_sdk_elastic_load_balancing_v2.types.action_type_enum.deserialize_query(
                child_type
            )
        )
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_authenticate_oidc_config = el.find("AuthenticateOidcConfig")
    if child_authenticate_oidc_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_config

        out["authenticate_oidc_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_config.deserialize_query(
                child_authenticate_oidc_config
            )
        )
    child_authenticate_cognito_config = el.find("AuthenticateCognitoConfig")
    if child_authenticate_cognito_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_config

        out["authenticate_cognito_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_config.deserialize_query(
                child_authenticate_cognito_config
            )
        )
    child_order = el.find("Order")
    if child_order is not None:
        out["order"] = int(child_order.text or "")
    child_redirect_config = el.find("RedirectConfig")
    if child_redirect_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.redirect_action_config

        out["redirect_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.redirect_action_config.deserialize_query(
                child_redirect_config
            )
        )
    child_fixed_response_config = el.find("FixedResponseConfig")
    if child_fixed_response_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.fixed_response_action_config

        out["fixed_response_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.fixed_response_action_config.deserialize_query(
                child_fixed_response_config
            )
        )
    child_forward_config = el.find("ForwardConfig")
    if child_forward_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.forward_action_config

        out["forward_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.forward_action_config.deserialize_query(
                child_forward_config
            )
        )
    child_jwt_validation_config = el.find("JwtValidationConfig")
    if child_jwt_validation_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_config

        out["jwt_validation_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_config.deserialize_query(
                child_jwt_validation_config
            )
        )
    return out
