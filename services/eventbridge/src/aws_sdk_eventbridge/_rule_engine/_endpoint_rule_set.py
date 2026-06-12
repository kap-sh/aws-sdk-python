from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    get_attr,
    interpolate,
    is_valid_host_label,
    string_equals,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseDualStack: bool | None = None,
        UseFIPS: bool | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
        EndpointId: str | None = None,
    ):
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.EndpointId = EndpointId if EndpointId is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if not (p.Endpoint is not None):
        if p.Region is not None:
            _locals["PartitionResult"] = aws_partition(p.Region)
            if _locals["PartitionResult"] is not None:
                if string_equals(
                    get_attr(
                        _locals["PartitionResult"], interpolate("name", p, _locals)
                    ),
                    interpolate("aws-us-gov", p, _locals),
                ):
                    if p.UseFIPS is True:
                        if p.UseDualStack is True:
                            return Endpoint(
                                url=interpolate(
                                    "https://events.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
    _locals: dict[str, Any] = {}
    if p.EndpointId is not None:
        if p.Region is not None:
            _locals["PartitionResult"] = aws_partition(p.Region)
            if _locals["PartitionResult"] is not None:
                if is_valid_host_label(p.EndpointId, True):
                    if p.UseFIPS is False:
                        if p.Endpoint is not None:
                            return Endpoint(
                                url=p.Endpoint,
                                properties={
                                    "authSchemes": [
                                        {
                                            "name": interpolate("sigv4a", p, _locals),
                                            "signingName": interpolate(
                                                "events", p, _locals
                                            ),
                                            "signingRegionSet": [
                                                interpolate("*", p, _locals)
                                            ],
                                        }
                                    ]
                                },
                                headers={},
                            )
                        if p.UseDualStack is True:
                            if True is get_attr(
                                _locals["PartitionResult"],
                                interpolate("supportsDualStack", p, _locals),
                            ):
                                return Endpoint(
                                    url=interpolate(
                                        "https://{EndpointId}.endpoint.events.{PartitionResult#dualStackDnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "authSchemes": [
                                            {
                                                "name": interpolate(
                                                    "sigv4a", p, _locals
                                                ),
                                                "signingName": interpolate(
                                                    "events", p, _locals
                                                ),
                                                "signingRegionSet": [
                                                    interpolate("*", p, _locals)
                                                ],
                                            }
                                        ]
                                    },
                                    headers={},
                                )
                            raise EndpointError(
                                interpolate(
                                    "DualStack is enabled but this partition does not support DualStack",
                                    p,
                                    _locals,
                                )
                            )
                        return Endpoint(
                            url=interpolate(
                                "https://{EndpointId}.endpoint.events.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4a", p, _locals),
                                        "signingName": interpolate(
                                            "events", p, _locals
                                        ),
                                        "signingRegionSet": [
                                            interpolate("*", p, _locals)
                                        ],
                                    }
                                ]
                            },
                            headers={},
                        )
                    raise EndpointError(
                        interpolate(
                            "Invalid Configuration: FIPS is not supported with EventBridge multi-region endpoints.",
                            p,
                            _locals,
                        )
                    )
                raise EndpointError(
                    interpolate("EndpointId must be a valid host label.", p, _locals)
                )
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.UseFIPS is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: FIPS and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        if p.UseDualStack is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: Dualstack and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if p.UseFIPS is True:
                if p.UseDualStack is True:
                    if True is get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    ):
                        if True is get_attr(
                            _locals["PartitionResult"],
                            interpolate("supportsDualStack", p, _locals),
                        ):
                            return Endpoint(
                                url=interpolate(
                                    "https://events-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                    raise EndpointError(
                        interpolate(
                            "FIPS and DualStack are enabled, but this partition does not support one or both",
                            p,
                            _locals,
                        )
                    )
            if p.UseFIPS is True:
                if (
                    get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    )
                    is True
                ):
                    if string_equals(
                        p.Region, interpolate("us-gov-east-1", p, _locals)
                    ):
                        return Endpoint(
                            url=interpolate(
                                "https://events.us-gov-east-1.amazonaws.com", p, _locals
                            ),
                            properties={},
                            headers={},
                        )
                    if string_equals(
                        p.Region, interpolate("us-gov-west-1", p, _locals)
                    ):
                        return Endpoint(
                            url=interpolate(
                                "https://events.us-gov-west-1.amazonaws.com", p, _locals
                            ),
                            properties={},
                            headers={},
                        )
                    return Endpoint(
                        url=interpolate(
                            "https://events-fips.{Region}.{PartitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "FIPS is enabled but this partition does not support FIPS",
                        p,
                        _locals,
                    )
                )
            if p.UseDualStack is True:
                if True is get_attr(
                    _locals["PartitionResult"],
                    interpolate("supportsDualStack", p, _locals),
                ):
                    return Endpoint(
                        url=interpolate(
                            "https://events.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "DualStack is enabled but this partition does not support DualStack",
                        p,
                        _locals,
                    )
                )
            return Endpoint(
                url=interpolate(
                    "https://events.{Region}.{PartitionResult#dnsSuffix}", p, _locals
                ),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
