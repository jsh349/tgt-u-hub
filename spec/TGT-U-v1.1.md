# TGT-U v1.1 (Unified)
- 용어 고정: superposition/interference/collapse, Φ(계획장), φ(물리 위상) 구분
- 코어식:
  Φ_{t+1}=Φ_t+Δt[iV_t-κΔΦ_t-λC_gauge/topo]
  J_collapse: i* = argmin_i (S_i + ξ||T(∇φ_i)|| + λ_r·RényiRisk), s.t. J_barrier>0
  T(∇Φ)=Σ_k β_k ∇Φ_k log(1+1/d_k) (+ ζ||z_PH||)
- 모듈: encode→estimate_field→propose→collapse→micro→memory.update
- 출력 순서: (1) 핵심식 (2) JSON/YAML (3) KPI/불변성 (4) 버전/시드/플래그
